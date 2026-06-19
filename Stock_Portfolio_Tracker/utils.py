import csv
from datetime import datetime


def save_to_csv(data):

    file_name="portfolio_history.csv"

    with open(
        file_name,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer=csv.writer(file)

        writer.writerow(
            [
                "Date",
                "Stock",
                "Quantity",
                "BuyPrice",
                "Investment",
                "CurrentPrice",
                "ProfitLoss"
            ]
        )


        for item in data:

            writer.writerow(

                [

                datetime.now(),

                item["stock"],

                item["quantity"],

                item["buy_price"],

                item["total"],

                item["current_price"],

                item["profit_loss"]

                ]
            )