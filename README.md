# gamebot

Gotchas:

Getting a Hello World to work on localhost (front-end + backend) is quite a mission.

There's a persistent CORS error, that can be seen in Chrome DevTools when you click the button, making the request.

🔹 The first suggestion from GPT4 is to actually _serve_ the frontend, rather than simply opening the index.html in Chrome (which results in an origin of None rather than localhost:port)

This is done by (from the frontend folder) doing: `python -m http.server`
That will serve a frontend on port 8000, so open a Chrome tab at: http://localhost:8000/

🔹 There's an initial warning/error due to lack of favicon.ico (which seems to be a universally expected file, I think it's the icon that appears in the browser window). Just creating an empty file (temp) fixes.

After this ensued a long conversation with GPT4:

https://chat.openai.com/share/a4a40397-2ce1-4637-b4e6-3d3893ff2c65

🔹 One issue was that my backend port (5000) was already in use by my MacOS. There's some core service that uses it, so it's a really bad default choice.

(.venv) 
🧢 pi@pis-MacBook-Pro ~/code/2023/CM/YeTian-boardgames/gamebot (main)
> lsof -i :5000
COMMAND     PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
ControlCe   912   pi    7u  IPv4 0xa61a90c12814dd69      0t0  TCP *:commplex-main (LISTEN)
ControlCe   912   pi    8u  IPv6 0xa61a90b78f11f7a1      0t0  TCP *:commplex-main (LISTEN)
ControlCe   912   pi   13u  IPv6 0xa61a90b78c289fa1      0t0  TCP localhost:commplex-main->localhost:54877 (ESTABLISHED)
Google     1108   pi   31u  IPv6 0xa61a90b78c288fa1      0t0  TCP localhost:54877->localhost:commplex-main (ESTABLISHED)
python3.1 25572   pi    3u  IPv4 0xa61a90c128114029      0t0  TCP localhost:commplex-main (LISTEN)
python3.1 25573   pi    3u  IPv4 0xa61a90c128114029      0t0  TCP localhost:commplex-main (LISTEN)
python3.1 25573   pi    4u  IPv4 0xa61a90c128114029      0t0  TCP localhost:commplex-main (LISTEN)
(.venv) 
🧢 pi@pis-MacBook-Pro ~/code/2023/CM/YeTian-boardgames/gamebot (main)
> lsof -i :8000
COMMAND     PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
python3.1 24646   pi    4u  IPv6 0xa61a90b78c2887a1      0t0  TCP *:irdmi (LISTEN)
(.venv) 

Solution here is to specify a different port from which the backend is to be served, and update the frontend code accordingly. I've chosen 15007:
```
    app.run(debug=True, port=15007)
```

Now this STILL doesn't shake it loose, and I ended up having to go back to the stone age, sorry, Google / StackOverflow, and splat a couple of articles into GPT4.

🔹 The final fix was indeed a modification to the CORS line:

```
app = Flask(__name__)
# CORS(app)
# CORS(app, origins='*', methods='*', allow_headers=['Content-Type'])
# CORS(app, origins=['http://localhost:8000'], methods='*', allow_headers=['Content-Type'], supports_credentials=True)

CORS(app, origins='*', methods=['POST', 'OPTIONS'], allow_headers=['Content-Type', 'Authorization'], supports_credentials=True)
```

Now that it's working, a reasonable next step would be to incrementally push the code back towards a minimal Hello World, and identify the crucial code change(s).
