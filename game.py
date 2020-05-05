import random

# 预计排序在显示手牌时

##---compare card---##
# if card1 bigger, return 1


def card_cmp(card1, card2):
    if (len(card1) == 1 and len(card2) == 2):
        return 1
    if (len(card1) == 2 and len(card2) == 1):
        return 0
    if (len(card1) == 1 and len(card2) == 1):
        if (ord(card1) >= ord(card2)):
            return 1
        if (ord(card1) < ord(card2)):
            return 0
    if (len(card1) == 2 and len(card2) == 2):
        if (ord(card1[1]) > ord(card2[1])):
            return 1
        if (ord(card1[1]) < ord(card2[1])):
            return 0
        if (ord(card1[1]) == ord(card2[1])):
            if (card1[0] >= card2[0]):
                return 1
            if (card1[0] < card2[0]):
                return 0


def sort_card(card_pile):
    for i in range(1, len(card_pile)):
        for j in range(0, len(card_pile)-i):
            if (card_cmp(card_pile[j], card_pile[j+1])):
                card_pile[j], card_pile[j+1] = card_pile[j+1], card_pile[j]


class Player:
    hand_number_normal = 12
    hand_number_get = 13

    def __init__(self, pile):
        self.hand = self.ini_draw(pile)

    def ini_draw(self, pile):
        out_hand = list()
        for _ in range(0, 13):
            r = random.randint(0, len(pile)-1)
            temp = pile[r]
            pile.pop(r)
            out_hand.append(temp)
        return out_hand

    def ShowHand(self):
        sort_card(self.hand)
        temp_hand = str()
        for i in range(0, len(self.hand)):
            temp_hand += self.hand[i]
            temp_hand += ' '
        print(temp_hand)

    def PlayCard(self, waste_pile):
        card_num = int(input("discard:"))-1
        waste_pile.append(self.hand[card_num])
        self.hand.pop(card_num)

    def DrawCard(self, pile):
        r = random.randint(0, len(pile)-1)
        temp = pile[r]
        pile.pop(r)
        self.hand.append(temp)
    
    def RonJudge(self):
        return 1


#---intialize pile---#
pile_mount = list()
for _ in range(4):
    for i in range(1, 10):
        pile_mount.append(str(i)+'筒')
        pile_mount.append(str(i)+'索')
        pile_mount.append(str(i)+'万')
    pile_mount.append('东')
    pile_mount.append('南')
    pile_mount.append('西')
    pile_mount.append('北')
    pile_mount.append('中')
    pile_mount.append('発')
    pile_mount.append('白')

#---initialize waste pile#
waste_1 = list()

#---player draw card---#

# for i in range(0, 236):
#     print(pile_mount[i])
# print(len(pile_mount))
player_1 = Player(pile_mount)
player_2 = Player(pile_mount)
player_3 = Player(pile_mount)
player_4 = Player(pile_mount)

player_1.ShowHand()
# player_2.ShowHand()
# player_3.ShowHand()
# player_4.ShowHand()

#---play trial---#
while(Player.RonJudge(player_1)):
    player_1.PlayCard(waste_1)
    player_1.ShowHand()
    player_1.DrawCard(pile_mount)
    player_1.ShowHand()