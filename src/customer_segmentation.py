import matplotlib.pyplot as plt


def customer_segmentation_chart(rfm):
    segment_counts = rfm["Segment"].value_counts()

    print("\nCustomer Segment Counts:\n")
    print(segment_counts)

    plt.figure(figsize=(8, 5))
    segment_counts.plot(kind="bar")

    plt.title("Customer Segmentation")
    plt.xlabel("Segment")
    plt.ylabel("Number of Customers")

    plt.xticks(rotation=20)

    plt.tight_layout()
    plt.show()