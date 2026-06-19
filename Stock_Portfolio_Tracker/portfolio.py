from stocks import stock_prices
from utils import save_to_csv
import random


class Portfolio:

    def __init__(self):

        self.investments=[]


    def start(self):

        while True:

            print("\nAvailable Stocks:")

            for stock,price in stock_prices.items():

                print(
                    f"{stock} : ${price}"
                )

            stock=input(
                "\nEnter stock name: "
            ).upper()


            if stock not in stock_prices:

                print(
                    "❌ Stock not found"
                )

                continue


            try:

                quantity=int(
                    input(
                        "Enter quantity: "
                    )
                )

            except:

                print(
                    "Invalid quantity"
                )

                continue


            price=stock_prices[stock]

            total=price*quantity


            simulated_change=random.randint(
                -20,
                20
            )

            current_price=price+simulated_change

            profit_loss=(
                current_price-price
            )*quantity


            investment={

                "stock":stock,
                "quantity":quantity,
                "buy_price":price,
                "total":total,
                "current_price":current_price,
                "profit_loss":profit_loss
            }

            self.investments.append(
                investment
            )


            choice=input(
                "\nAdd another stock? (yes/no): "
            ).lower()

            if choice!="yes":
                break


        self.show_summary()


    def show_summary(self):

        print("\n")
        print("="*60)
        print("PORTFOLIO SUMMARY")
        print("="*60)

        grand_total=0
        total_profit=0


        for item in self.investments:

            print(
                f"""
Stock: {item['stock']}
Quantity: {item['quantity']}
Buy Price: ${item['buy_price']}
Investment: ${item['total']}
Current Price: ${item['current_price']}
Profit/Loss: ${item['profit_loss']}
"""
            )

            grand_total+=item['total']

            total_profit+=item['profit_loss']


        print("="*60)

        print(
            f"Total Investment: ${grand_total}"
        )

        print(
            f"Total Profit/Loss: ${total_profit}"
        )


        save_to_csv(
            self.investments
        )

        print(
            "\n✅ Portfolio saved"
        )