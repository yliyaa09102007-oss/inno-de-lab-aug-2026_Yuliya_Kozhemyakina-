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
ssl_settings_default = db_config["connection"].get("ssl_settings", "verify-full")
print(f"SSL Mode: {ssl_settings_default}")

#changing and adding info
db_config["connection"]["user"] = "admin"
db_config["connection"]["max_connections"] = 100

#printing "connection" using .items()
print("Параметры соединения:")
for k, v in db_config["connection"].items():
    print(f"* {k}: {v}")