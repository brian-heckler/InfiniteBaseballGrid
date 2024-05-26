from quart import Quart, request, jsonify, Response
from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

#database_connection_string = os.getenv("DB_CONNECTION_STRING")
database_connection_string = os.getenv("mongodb+srv://bheckler24:dyEtBbNrv1YFmoqk@magic-doku.gzi2n0j.mongodb.net/?retryWrites=true&w=majority&appName=magic-doku")
dev_ip = os.getenv("DEV_IP")

dev = True
if dev:
    from GameCategories import GameCategories
    from BaseballData import BaseballData
    from Database import Database
else:
    from server.GameCategories import GameCategories
    from server.BaseballData import BaseballData
    from server.Database import Database
import datetime

mongo_client = AsyncIOMotorClient('mongodb+srv://bheckler24:dyEtBbNrv1YFmoqk@magic-doku.gzi2n0j.mongodb.net/?retryWrites=true&w=majority&appName=magic-doku')
db: Database = Database(mongo_client, dev)

app = Quart(__name__)

@app.after_request
async def after_request(response):
    if dev:
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    else:
        allowed_origins = [
            "https://www.infiniteimmaculategrid.com",
            "https://www.infinitebaseballgrid.com"
        ]
        
        origin = request.headers.get('Origin')
        
        if origin and origin in allowed_origins:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        
        return response

@app.route("/get_new_grid", methods=["GET"])
async def get_new_grid():
    categories: GameCategories = GameCategories()
    return jsonify(categories.get_grid())

@app.route("/get_current_grid", methods=["GET"])
async def get_current_grid():
    categories: GameCategories = GameCategories()
    return jsonify(categories.get_grid())

@app.route("/search_players", methods=["GET"])
async def search_players():
    query: str = request.args.get("name")
    players: list = await BaseballData.search_players(query)
    data: list = players
    if len(data) > 0:
        if len(data) > 5:
            data = data[:5]
        players: list = []
        for x in range(len(data)):
            start: str = ''
            end: str = ''
            try:
                if data[x]['reprint']:
                    #original_printing = await BaseballData.search_reprints(data[x])
                    #start = original_printing['released_at'][:4] # reprint date
                    #end = data[x]['released_at'][:4] # most recent print date
                    start = ''
                    end = ''
                    #start = data[x]['released_at'][:4]
                    #end = datetime.datetime.now().year
                else:
                    #start = data[x]['released_at'][:4]
                    #end = data[x]['released_at'][:4]
                    start = ''
                    end = ''
                #players.append(data[x]["name"] + f" | ({start}-{end})") 
                players.append(data[x]["name"])
            except KeyError:
                players.append(data[x]["name"])
        return jsonify(players)
    return jsonify([])

@app.route("/validate_player", methods=["GET"])
async def validate_player():
    query = request.args.get("name")
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    hardMode = request.args.get("hardMode")
    team3 = request.args.get("team3") # hardmode category
    start = request.args.get("start")
    end = request.args.get("end")
    players = await BaseballData.search_players(query)
    player = ''
    if len(players) > 1:
        for x in range(len(players)):
            if players[x]["name"] == query:
                try:
                    if players[x]['reprint']:
                        if start == players[x]['released_at'][:4]:
                            player = players[x]
                    else:
                        if start == players[x]['released_at'][:4] and end == players[x]['released_at'][:4]:
                            player = players[x]
                except KeyError:
                    continue
    else: player = players[0]
    teams = BaseballData.get_player_teams(player)
    if player["reprint"]:
        reprint_sets = await BaseballData.search_reprints(player)
        for set in reprint_sets:
            if set not in teams:
                teams.append(BaseballData.__get_old_set_names(set))
        #teams.extend(BaseballData._BaseballData__get_old_set_names(reprint_sets))
        #teams.append(original_printing["set_name"])
    if teams:
        #if team1 in teams and team2 in teams:
        if hardMode == 'true' and team1 in teams and team2 in teams and team3 in teams: # temp code to accept any entry
            picture = BaseballData.get_player_picture(player)
            name = player["name"]
            id = player['id'] #.split('/')[-1]
            await db.update_matchup(teams=(team1, team2), player=name, id=id)
            rarity_score = await db.calculate_rarity_score(teams=(team1, team2), player=name, id=id)
            #rarity_score = 95 # placeholder value
            return jsonify({"picture": picture, "name": name, "rarity_score": rarity_score})
        
        if hardMode == 'false' and team1 in teams and team2 in teams: # temp code to accept any entry
            picture = BaseballData.get_player_picture(player)
            name = player["name"]
            id = player['id'] #.split('/')[-1]
            await db.update_matchup(teams=(team1, team2), player=name, id=id)
            rarity_score = await db.calculate_rarity_score(teams=(team1, team2), player=name, id=id)
            #rarity_score = 95 # placeholder value
            return jsonify({"picture": picture, "name": name, "rarity_score": rarity_score})
    # return nothing
    return jsonify({})

@app.route("/set_shared_grid", methods=["POST"])
async def set_shared_grid():
    data = await request.get_json()
    grid = data["grid"]
    id = await db.set_shared_grid(grid)
    return jsonify({"id": id})

@app.route("/get_shared_grid", methods=["GET"])
async def get_shared_grid():
    id = request.args.get("id")
    grid = await db.get_shared_grid(id)
    if grid == []:
        return Response(status=404)
    return jsonify(grid)

@app.route("/get_top_players", methods=["POST"])
async def get_top_players():
    data = await request.get_json()
    grid = data["grid"]
    matchups = GameCategories.get_matchups(grid)
    top_players = [[], [], []]
    for i in range(9):
        if len(top_players[i%3]) < 3:
            player = await db.get_top_player(matchups[i])
            if player:
                top_players[i%3].append(player)
    return jsonify(top_players)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)