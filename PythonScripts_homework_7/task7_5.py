import json #importing json to print the dictionary

system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]
active_nodes = []
cpu_list = []
ram_list = []

#finding online nodes and creating a list for every metric
for nodes in system_telemetry:
    node_name, cpu, ram, status = nodes
    if status != "offline":
        active_nodes.append(node_name)
        cpu_list.append(cpu)
        ram_list.append(ram)

metrics_dict = {
    "active_nodes_count" : len(active_nodes),
    "metrics": {
        "average_cpu": round(sum(cpu_list)/len(cpu_list),2),
        "max_ram": max(ram_list)
    }
}

#printing the result
print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчёт телеметрии:")
#found this method to print the dictionary so it's readable
print(json.dumps(metrics_dict, indent=4))

