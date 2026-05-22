import sys
from agent.main_agent import ask_agent

def main():
    print("====================================================")
    print(" 🇧🇩 Bangladesh Multi-Tool AI Agent Engine Active 🇧🇩 ")
    print("====================================================")
    print("Ask data queries about Hospitals, Restaurants, or Schools.")
    print("Type 'exit' or 'quit' to terminate application session.\n")

    while True:
        try:
            query = input("Ask: ").strip()
            if not query:
                continue
                
            if query.lower() in ["exit", "quit"]:
                print("\nShutting down session safely. Good luck with your assignment submission!")
                break

            print("\n Processing query via LangChain Routing Executor...")
            response = ask_agent(query)
            print(f"\n Answer:\n{response}\n")
            print("-" * 52)
            
        except KeyboardInterrupt:
            print("\nSession safely interrupted.")
            sys.exit(0)

if __name__ == "__main__":
    main()