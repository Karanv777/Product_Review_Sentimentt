from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment = SentimentIntensityAnalyzer()

while(True):
    print("For review -- Press 1\n")
    print("To exit -- Press any key\n")
    x = input("Enter choice == ")

    if x == '1':
        text_1 = input("\nEnter your review for the product : ")

        sent_1 = sentiment.polarity_scores(text_1)

        try:
            if sent_1["compound"] <= -0.5:
                print("Negative 😡\n")

            elif sent_1["compound"] >= 0.5:
                print("Positive 😍\n")

            else:
                print("Neutral 😐\n")

        except Exception as e:
            print(e)

    else:
        print("\nProgram Closed!")
        break        

# import sys; print(sys.path)
