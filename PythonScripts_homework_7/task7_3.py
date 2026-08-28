db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}
#getting the values
host_value = db_config["connection"]["host"]
port_value = db_config["connection"]["port"]

#safely checking if there is a value for key "ssl_settings"
ssl_settings = db_config["connection"].get("ssl_settings")

if ssl_settings is None:
    ssl_mode = "verify-full"
else:
    ssl_mode = ssl_settings.get("ssl_mode", "verify-full")

print(f"SSL Mode: {ssl_mode}")

#changing and adding info
db_config["connection"]["user"] = "admin"
db_config["connection"]["max_connections"] = 100

#printing "connection" using .items()
print("Параметры соединения:")
for k, v in db_config["connection"].items():
    print(f"* {k}: {v}")