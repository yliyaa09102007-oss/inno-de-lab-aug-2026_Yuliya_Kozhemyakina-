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

#printing the result (not sure how to do it differently, I feel like I hardcoded it but ok)
print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчёт телеметрии:")
print("{\n"
    "active_nodes_count: " + str(len(active_nodes)) + ",\n"
    "'metrics': {\n"
    "   'average_cpu': " + str(round(sum(cpu_list)/len(cpu_list),2)) + ",\n"
    "   'max_ram': " + str(max(ram_list)) + "\n"
    "   }\n"
    "}")

