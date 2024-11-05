
gift = [boxes[0]]
for box in boxes[1:]:
    if gift[-1] - box >= 5:
        gift.append(box)
print(len(gift), min(gift))