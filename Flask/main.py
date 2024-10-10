from flask import Flask, request

app = Flask(__name__) 
 

@app.route('/') 
def display_file(): 
    file_path = request.args.get('file') 
    if file_path: 
        try: 
            with open(file_path, 'r') as file: 
                content = file.read() 
            return f"<pre>{content}</pre>" 
        except FileNotFoundError: 
            return "File not found", 404 
        except Exception as e: 
            return f"Error: {e}", 500 
    else: 
        return "No file specified", 400 
 
@app.route('/path')
def get_flask_path():
    try:
        return f"""public bits: [<br><br>
                Name: see /etc/passwd/, and copy name // username {{username}}:x:1000:1000:{{username}},,,:/home/{{username}}:/usr/bin/sh <br><br>
                ModName: {app.__module__} // getattr(app, "__module__", t.cast(object, app).__class__.__module__) <br><br>
                Flask Name: Flask // getattr(app, "__name__", type(app).__name__) <br><br>
                Path to Flask: go to path "/error" and copy path to "app.py" // getattr(mod, "__file__", None) <br><br>]
                <br><br><br>
                private_bits: [<br><br>
                Mac Addres To DEC: copy text from /sys/class/net/eth0/address and convert to DEC (if not valid pin, try wlan0, and more) <br>
                machine_id: copy text from /etc/machine-id 
                <br><br>]
    

                """, 200
    except Exception as ex:
        return f"ERROR: {ex}", 500

@app.route('/error')
def error():
    return f"{app.__marcus__}" 


if __name__ == '__main__': 
    app.run(debug=True)
