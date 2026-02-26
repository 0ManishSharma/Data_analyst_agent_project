from agent import create_agent

if __name__ == "__main__":
    agent = create_agent()

    question = "Show top 5 products by total revenue"
    response = agent.invoke({"input": question})

    print("\nAI Response:")
    print(response["output"])