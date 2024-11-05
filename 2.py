f = open("26.2.txt")
n = int(f.readline())
boxes = [int(s) for s in f]
boxes.sort(reverse=True)
blocks = []
while boxes != []:
    gift = [boxes[0]]
    del boxes[0]
    for box in boxes[:]:
        if gift[-1] - box >= 5:
            gift.append(box)
            boxes.remove(box)
    blocks.append(gift)
print(len(blocks), len(blocks[0]))
