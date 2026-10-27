
knowledge_base = {
    "refund": "Refunds are processed within 5-7 business days after approval.",
    "delivery": "Standard delivery usually takes 3-5 business days.",
    "password": "Use the Forgot Password option to reset your password.",
    "return": "Products can be returned within 7 days of delivery."
}

orders = {
    "ORD101": "Shipped",
    "ORD102": "Delivered",
    "ORD103": "Processing"
}


def search_knowledge_base(query):
    for keyword, answer in knowledge_base.items():
        if keyword in query.lower():
            return answer
    return None


def check_order(order_id):
    return orders.get(order_id.upper(), "Order not found")


def escalate_to_human(query):
    return f"Your issue has been forwarded to human support: {query}"


def agent(query):
    print("\nAgent: Analyzing your request...")

    if "order" in query.lower() and any(
        order_id in query.upper() for order_id in orders
    ):
        order_id = next(
            order_id for order_id in orders if order_id in query.upper()
        )
        print("Action: Using order tracking tool")
        return check_order(order_id)

    answer = search_knowledge_base(query)

    if answer:
        print("Action: Searching the knowledge base")
        return answer

    print("Action: Escalating to human support")
    return escalate_to_human(query)


print("Agentic AI Customer Support Assistant")
print("Ask a question or type 'exit' to stop.")

while True:
    user_query = input("\nYou: ")

    if user_query.lower().strip() == "exit":
        print("Agent: Goodbye!")
        break

    print("Agent:", agent(user_query))
