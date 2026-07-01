from agents.root_agent import root_agent

print(root_agent.name)

print()

print("Sub Agents:")

for agent in root_agent.sub_agents:
    print(agent.name)