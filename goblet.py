def win_check(player2_red,player1_white,banmen2_out_int):
    a = player2_red[0]
    b = player1_white[11]
    c = player1_white[0]
    retu_number = 4
    gyou_number = 4

    for i in range(retu_number): #列確認
        if ((banmen2_out_int[0][i]>=a and banmen2_out_int[1][i]>=a and banmen2_out_int[2][i]>=a and banmen2_out_int[3][i]>=a) or
        ((banmen2_out_int[0][i]>=c and banmen2_out_int[0][i]<=b) and (banmen2_out_int[1][i]>=c and banmen2_out_int[1][i]<=b) and (banmen2_out_int[2][i]>=c and banmen2_out_int[2][i]<=b) and (banmen2_out_int[3][i]>=c and banmen2_out_int[3][i]<=b))):
            return True

    for j in range(gyou_number):  #行確認
        if ((banmen2_out_int[j][0]>=a and banmen2_out_int[j][1]>=a and banmen2_out_int[j][2]>=a and banmen2_out_int[j][3]>=a) or
        ((banmen2_out_int[j][0]>=c and banmen2_out_int[j][0]<=b) and (banmen2_out_int[j][1]>=1 and banmen2_out_int[j][1]<=b) and (banmen2_out_int[j][2]>=c and banmen2_out_int[j][2]<=b) and (banmen2_out_int[j][3]>=c and banmen2_out_int[j][3]<=b))):
            return True

    #斜め確認
    if (banmen2_out_int[0][3]>=a and banmen2_out_int[1][2]>=a and banmen2_out_int[2][1]>=a and banmen2_out_int[3][0]>=a or
    banmen2_out_int[0][0]>=a and banmen2_out_int[1][1]>=a and banmen2_out_int[2][2]>=a and banmen2_out_int[3][3]>=a or
    (banmen2_out_int[0][3]>=c and banmen2_out_int[0][3]<=b) and (banmen2_out_int[1][2]>=c and banmen2_out_int[1][2]<=b) and (banmen2_out_int[2][1]>=c and banmen2_out_int[2][1]<=b) and (banmen2_out_int[3][0]>=c and banmen2_out_int[3][0]<=b) or
    (banmen2_out_int[0][0]>=c and banmen2_out_int[0][0]<=b) and (banmen2_out_int[1][1]>=c and banmen2_out_int[1][1]<=b) and (banmen2_out_int[2][2]>=c and banmen2_out_int[2][2]<=b) and (banmen2_out_int[3][3]>=c and banmen2_out_int[3][3]<=b)):
        return True

    else:
        return False

def winer_which(banmen2_out_int):
    a=player2_red[0]
    b=player1_white[11]
    c=player1_white[0]
    retu_number=4
    gyou_number=4
    RED = '\033[31m'
    END = '\033[0m'
    red=RED+"赤"+END

    for i in range(retu_number):
        if (banmen2_out_int[0][i]>=a and banmen2_out_int[1][i]>=a and banmen2_out_int[2][i]>=a and banmen2_out_int[3][i]>=a):
            return red

        if ((banmen2_out_int[0][i]>=c and banmen2_out_int[0][i]<=b) and (banmen2_out_int[1][i]>=c and banmen2_out_int[1][i]<=b) and (banmen2_out_int[2][i]>=c and banmen2_out_int[2][i]<=b) and (banmen2_out_int[3][i]>=c and banmen2_out_int[3][i]<=b)):
            return "白"

    for j in range(gyou_number):
        if (banmen2_out_int[j][0]>=a and banmen2_out_int[j][1]>=a and banmen2_out_int[j][2]>=a and banmen2_out_int[j][3]>=a):
            return red

        if ((banmen2_out_int[j][0]>=c and banmen2_out_int[j][0]<=b) and (banmen2_out_int[j][1]>=c and banmen2_out_int[j][1]<=b) and (banmen2_out_int[j][2]>=c and banmen2_out_int[j][2]<=b) and (banmen2_out_int[j][3]>=c and banmen2_out_int[j][3]<=b)):
            return "白"

    if (banmen2_out_int[0][3]>=a and banmen2_out_int[1][2]>=a and banmen2_out_int[2][1]>=a and banmen2_out_int[3][0]>=a or
    banmen2_out_int[0][0]>=a and banmen2_out_int[1][1]>=a and banmen2_out_int[2][2]>=a and banmen2_out_int[3][3]>=a):
        return red

    if ((banmen2_out_int[0][3]>=c and banmen2_out_int[0][3]<=b) and (banmen2_out_int[1][2]>=c and banmen2_out_int[1][2]<=b) and (banmen2_out_int[2][1]>=c and banmen2_out_int[2][1]<=b) and (banmen2_out_int[3][0]>=c and banmen2_out_int[3][0]<=b) or
    (banmen2_out_int[0][0]>=c and banmen2_out_int[0][0]<=b) and (banmen2_out_int[1][1]>=c and banmen2_out_int[1][1]<=b) and (banmen2_out_int[2][2]>=c and banmen2_out_int[2][2]<=b) and (banmen2_out_int[3][3]>=c and banmen2_out_int[3][3]<=b)):
        return "白"

def exist_check(player_change_basic_count):
    a=player2_red[0]
    b=player1_white[11]
    c=player1_white[0]
    d=player2_red[11]
    retu_number=4
    gyou_number=4

    if player_change_basic_count%2==0:
        for i in range(c,b+1,1):
            for j in range(gyou_number):
                for k in range(retu_number):
                    if banmen2_out_int[j][k]==i:
                        return True

        return False

    else:
        for i in range(a,d+1,1):
            for j in range(gyou_number):
                for k in range(retu_number):
                    if banmen2_out_int[j][k]==i:
                        return True

        return False

def hear_bord_true_or_outside_false(player1_or_player2_list,series,full_and_small,exist):
    if player1_or_player2_list==player1_white and player1_white_outside_stack[0][3]==0 and player1_white_outside_stack[1][3]==0 and player1_white_outside_stack[2][3]==0:
        print("外部のスタックがなくなりました。")
        return True

    if player1_or_player2_list==player2_red and player2_red_outside_stack[0][3]==0 and player2_red_outside_stack[1][3]==0 and player2_red_outside_stack[2][3]==0:
        print("外部のスタックがなくなりました。")
        return True

    if full_and_small==True:
        print("外部スタックは、現在盤上に置くことができません")
        return True
    
    if exist==False:
        return False

    if series==False and ((0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3])):
        return True

    input_check=False
    while input_check==False:
        input_bord_or_outside=""
        while input_bord_or_outside=="":
            input_bord_or_outside=input("外部スタックなら1を、盤上のスタックを動かすなら2を選択してください")
            if input_bord_or_outside=="":
                print("その選択肢はありません")

        if input_bord_or_outside=="1":
            return False

        if input_bord_or_outside=="2":
            return True

        else:
            print("その選択肢はありません")
            input_check=False

def series_check(player1_or_player2_list,player1_white,banmen2_out_int):
    if player1_or_player2_list==player1_white:
        for i in range(4):
            if (banmen2_out_int[0][i]>=21 and banmen2_out_int[1][i]>=21 and banmen2_out_int[2][i]>=21 or
            banmen2_out_int[1][i]>=21 and banmen2_out_int[2][i]>=21 and banmen2_out_int[3][i]>=21):
                return True

        for j in range(4):
            if (banmen2_out_int[i][0]>=21 and banmen2_out_int[i][1]>=21 and banmen2_out_int[i][2]>=21 or
            banmen2_out_int[i][1]>=21 and banmen2_out_int[i][2]>=21 and banmen2_out_int[i][3]>=21):
                return True 

        if (banmen2_out_int[0][3]>=21 and banmen2_out_int[1][2]>=21 and banmen2_out_int[2][1]>=21 or
        banmen2_out_int[1][2]>=21 and banmen2_out_int[2][1]>=21 and banmen2_out_int[3][0]>=21 or
        banmen2_out_int[0][0]>=21 and banmen2_out_int[1][1]>=21 and banmen2_out_int[2][2]>=21 or
        banmen2_out_int[1][1]>=21 and banmen2_out_int[2][2]>=21 and banmen2_out_int[3][3]>=21 ):
            return True

        else:
            return False

    else:
        for i in range(4):
            if (((banmen2_out_int[0][i]>=1 and banmen2_out_int[0][i]>=12) and (banmen2_out_int[1][i]>=1 and banmen2_out_int[1][i]>=12) and (banmen2_out_int[2][i]>=1 and banmen2_out_int[2][i]>=12)) or
            (banmen2_out_int[1][i]>=1 and banmen2_out_int[1][i]>=12) and (banmen2_out_int[2][i]>=1 and banmen2_out_int[2][i]>=12) and (banmen2_out_int[3][i]>=1 and banmen2_out_int[3][i]>=12)):
                return True

        for j in range(4): 
            if (((banmen2_out_int[i][0]>=1 and banmen2_out_int[i][0]>=12) and (banmen2_out_int[i][1]>=1 and banmen2_out_int[i][1]>=12) and (banmen2_out_int[i][2]>=1 and banmen2_out_int[i][2]>=12)) or
            ((banmen2_out_int[i][1]>=1 and banmen2_out_int[i][1]<=12) and (banmen2_out_int[i][2]>=1 and banmen2_out_int[i][2]<=12) and (banmen2_out_int[i][3]>=1 and banmen2_out_int[i][3]<=12))):
                return True

        if (((banmen2_out_int[0][3]>=1 and banmen2_out_int[0][3]<=12) and (banmen2_out_int[1][2]>=1 and banmen2_out_int[1][2]<=12) and (banmen2_out_int[2][1]>=1 and banmen2_out_int[2][1]<=12)) or
        ((banmen2_out_int[1][2]>=1 and banmen2_out_int[1][2]<=12) and (banmen2_out_int[2][1]>=1 and banmen2_out_int[2][1]<=12) and (banmen2_out_int[3][0]>=1 and banmen2_out_int[3][0]<=12)) or
        ((banmen2_out_int[0][0]>=1 and banmen2_out_int[0][0]<=12) and (banmen2_out_int[1][1]>=1 and banmen2_out_int[1][1]<=12) and (banmen2_out_int[2][2]>=1 and banmen2_out_int[2][2]<=12)) or
        ((banmen2_out_int[1][1]>=1 and banmen2_out_int[1][1]<=12) and (banmen2_out_int[2][2]>=1 and banmen2_out_int[2][2]<=12) and (banmen2_out_int[3][3]>=1 and banmen2_out_int[3][3]<=12))):
            return True

        else:
            return False
            
def player_change(player1_white,player2_red,player_change_basic_count):
    if player_change_basic_count%2==0:
        return player1_white

    else:
        return player2_red

def player_judge_name(player_change_basic_count):
    RED = '\033[31m'
    END = '\033[0m'
    a=RED+"赤"+END

    if player_change_basic_count%2==0:
        return "白"

    else:
        return a

def zahyo_move_input():
    zahyo_check=False
    while zahyo_check==False:
        zahyo=""
        while zahyo=="":
            zahyo=input("動かす駒が置かれている座標を入力してください")
            if zahyo=="":
                print("空白は入力できません")
                
        for i in range(16):
            if zahyo==str(i):
                zahyo_check=True

        if zahyo_check!=True:
            print("その座標は存在しません。もう一度入力してください")
            continue
        
    return zahyo

def coma_kind_check(banmen2_out_int,zahyo_puted):
    y=change_za_to_y(zahyo_puted)
    x=change_za_to_x(zahyo_puted)

    return banmen2_out_int[y][x]

def zahyo_input():
    zahyo_check=False
    while zahyo_check==False:
        zahyo=""
        while zahyo=="":
            zahyo=input("置く盤上の座標を入力してください")
            if zahyo=="":
                print("空白は座標ではありません")

        for i in range(16):
            if zahyo==str(i):
                zahyo_check=True

        if zahyo_check!=True:
            print("その座標は存在しません。もう一度入力してください")
            continue

    return zahyo

def men_change(zahyo,koma_size,zahyo_puted):
    if bord_true_or_outside_false==True:
        for i in range(4):
            if banmen1_pile[zahyo_puted][i]!=0:
                banmen1_pile[zahyo_puted][i]=0
                break

    for i in range(3,-1,-1):
        if banmen1_pile[zahyo][i]==0:
            banmen1_pile[zahyo][i]=koma_size
            break

    return banmen1_pile

def banmen2_form(banmen1_pile):
    for i in range(16):
        for j in range(4):
            x=change_za_to_x(i)
            y=change_za_to_y(i)
            if banmen1_pile[i][j]!=0:
                banmen2_out_int[y][x]=banmen1_pile[i][j]
                break

            if banmen1_pile[i][j]==0:
                banmen2_out_int[y][x]=0
      
    return banmen2_out_int

def coma_size_decide(player1_or_player2_list,choise_number):
    if player1_or_player2_list==player1_white:
        for i in range(4):
            if player1_white_outside_stack[choise_number][i]!=0:
                return player1_white_outside_stack[choise_number][i]
    
    else:
        for j in range(4):
            if player2_red_outside_stack[choise_number][j]!=0:
                return player2_red_outside_stack[choise_number][j]

def coma_kind_order(player1_or_player2_list,white_coma_kind_basic_count,red_coma_kind_basic_count):
    if player1_or_player2_list==player1_white:
        return white_coma_kind_basic_count

    else:
        return red_coma_kind_basic_count

def koma_judge(koma_size):
    if (koma_size==1 or koma_size==2 or koma_size==3 or 
    koma_size==21 or koma_size==22 or koma_size==23):
        toku="今から置くスタックの種類：特大"
        return toku

    elif (koma_size==4 or koma_size==5 or koma_size==6 or 
    koma_size==24 or koma_size==25 or koma_size==26):
        dai="今から置くスタックの種類：大"
        return dai

    elif (koma_size==7 or koma_size==8 or koma_size==9 or 
    koma_size==27 or koma_size==28 or koma_size==29):
        tyu="今から置くスタックの種類：中"
        return tyu

    elif (koma_size==10 or koma_size==11 or koma_size==12 or 
    koma_size==30 or koma_size==31 or koma_size==32):
        syo="今から置くスタックの種類：小"
        return syo

    else:
        over="スタックサイズ範囲外"
        return over
        
def can_put_judge_out(series,zahyo,coma_kind_int,banmen2_out_int):
    y=change_za_to_y(zahyo)
    x=change_za_to_x(zahyo)

    if (coma_kind_int>=10 and coma_kind_int<=12 and banmen2_out_int[y][x]!=0) or (coma_kind_int>=30 and coma_kind_int<=32 and banmen2_out_int[y][x]!=0):
        print("そこには置けません、もう一度入力してください")
        return False

    if series==False and banmen2_out_int[y][x]!=0:
        print("相手が3連続ではないため、そこには置けません。もう一度入力してください")
        return False

    if ((coma_kind_int>=7 and coma_kind_int<=9) and (banmen2_out_int[y][x]>=10 and banmen2_out_int[y][x]<=12 and series==True) or
    (coma_kind_int>=7 and coma_kind_int<=9) and (banmen2_out_int[y][x]>=30 and banmen2_out_int[y][x]<=32 and series==True) or
    (coma_kind_int>=4 and coma_kind_int<=6) and (banmen2_out_int[y][x]>=7 and banmen2_out_int[y][x]<=12 and series==True) or
    (coma_kind_int>=4 and coma_kind_int<=6) and (banmen2_out_int[y][x]>=27 and banmen2_out_int[y][x]<=32 and series==True) or
    (coma_kind_int>=1 and coma_kind_int<=3) and (banmen2_out_int[y][x]>=4 and banmen2_out_int[y][x]<=12 and series==True) or
    (coma_kind_int>=1 and coma_kind_int<=3) and (banmen2_out_int[y][x]>=24 and banmen2_out_int[y][x]<=32 and series==True) or
    (coma_kind_int>=27 and coma_kind_int<=29) and (banmen2_out_int[y][x]>=10 and banmen2_out_int[y][x]<=12 and series==True) or
    (coma_kind_int>=27 and coma_kind_int<=29) and (banmen2_out_int[y][x]>=30 and banmen2_out_int[y][x]<=32 and series==True) or
    (coma_kind_int>=24 and coma_kind_int<=26) and (banmen2_out_int[y][x]>=7 and banmen2_out_int[y][x]<=12 and series==True) or
    (coma_kind_int>=24 and coma_kind_int<=26) and (banmen2_out_int[y][x]>=27 and banmen2_out_int[y][x]<=32 and series==True) or
    (coma_kind_int>=21 and coma_kind_int<=23) and (banmen2_out_int[y][x]>=4 and banmen2_out_int[y][x]<=12 and series==True) or
    (coma_kind_int>=21 and coma_kind_int<=23) and (banmen2_out_int[y][x]>=24 and banmen2_out_int[y][x]<=32 and series==True)):
        return True

    if banmen2_out_int[y][x]==0:
        return True

    else:
        print("そこには置くことができません。もう一度入力してください")
        return False

def can_put_judge_ban(za,coma_kind_int,banmen2_out_int):
    y=change_za_to_y(za)
    x=change_za_to_x(za)

    if (((coma_kind_int>=10 and coma_kind_int<=12) or (coma_kind_int>=30 and coma_kind_int<=32)) and
    (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3])):
        print("そこには置けません、もう一度入力してください")
        return False

    if ((coma_kind_int>=7 and coma_kind_int<=9) and (banmen2_out_int[y][x]>=10 and banmen2_out_int[y][x]<=12) or
    (coma_kind_int>=7 and coma_kind_int<=9) and (banmen2_out_int[y][x]>=30 and banmen2_out_int[y][x]<=32) or
    (coma_kind_int>=4 and coma_kind_int<=6) and (banmen2_out_int[y][x]>=7 and banmen2_out_int[y][x]<=12) or
    (coma_kind_int>=4 and coma_kind_int<=6) and (banmen2_out_int[y][x]>=27 and banmen2_out_int[y][x]<=32) or
    (coma_kind_int>=1 and coma_kind_int<=3) and (banmen2_out_int[y][x]>=4 and banmen2_out_int[y][x]<=12) or
    (coma_kind_int>=1 and coma_kind_int<=3) and (banmen2_out_int[y][x]>=24 and banmen2_out_int[y][x]<=32) or
    (coma_kind_int>=27 and coma_kind_int<=29) and (banmen2_out_int[y][x]>=10 and banmen2_out_int[y][x]<=12) or
    (coma_kind_int>=27 and coma_kind_int<=29) and (banmen2_out_int[y][x]>=30 and banmen2_out_int[y][x]<=32) or
    (coma_kind_int>=24 and coma_kind_int<=26) and (banmen2_out_int[y][x]>=7 and banmen2_out_int[y][x]<=12) or
    (coma_kind_int>=24 and coma_kind_int<=26) and (banmen2_out_int[y][x]>=27 and banmen2_out_int[y][x]<=32) or
    (coma_kind_int>=21 and coma_kind_int<=23) and (banmen2_out_int[y][x]>=4 and banmen2_out_int[y][x]<=12) or
    (coma_kind_int>=21 and coma_kind_int<=23) and (banmen2_out_int[y][x]>=24 and banmen2_out_int[y][x]<=32)):
        return True

    if banmen2_out_int[y][x]==0:
        return True

    else:
        print("すでにおいてあるスタックの方が大きいため、置くことができません。もう一度、動かす駒を入力してください")
        return False

def men2_change_character(banmen2_out_int,banmen2_out_character):
    RED = '\033[31m'
    END = '\033[0m'
    a=RED+"特"+END
    b=RED+"大"+END
    c=RED+"中"+END
    d=RED+"小"+END

    for i in range(4):
        for j in range(4):
            if banmen2_out_int[i][j]==0:
                banmen2_out_character[i][j]="  "

            elif banmen2_out_int[i][j]>=1 and banmen2_out_int[i][j]<=3:
                banmen2_out_character[i][j]="特"

            elif banmen2_out_int[i][j]>=21 and banmen2_out_int[i][j]<=23:
                banmen2_out_character[i][j]=a

            elif banmen2_out_int[i][j]>=4 and banmen2_out_int[i][j]<=6:
                banmen2_out_character[i][j]="大"

            elif banmen2_out_int[i][j]>=24 and banmen2_out_int[i][j]<=26:
                banmen2_out_character[i][j]=b

            elif (banmen2_out_int[i][j]>=7 and banmen2_out_int[i][j]<=9):
                banmen2_out_character[i][j]="中"

            elif (banmen2_out_int[i][j]>=27 and banmen2_out_int[i][j]<=29):
                banmen2_out_character[i][j]=c

            elif (banmen2_out_int[i][j]>=10 and banmen2_out_int[i][j]<=12):
                banmen2_out_character[i][j]="小"

            elif (banmen2_out_int[i][j]>=30 and banmen2_out_int[i][j]<=32):
                banmen2_out_character[i][j]=d
                
    return banmen2_out_character

def change_za_to_y(i):
    if i//4==0:
        return 0

    elif i//4==1:
        return 1

    elif i//4==2:
        return 2

    elif i//4==3:
        return 3

def change_za_to_x(i):
    if i%4==0:
        return 0

    elif (i-1)%4==0:
        return 1

    elif (i-2)%4==0:
        return 2

    elif (i-3)%4==0:
        return 3

def can_move_judge(zahyo_puted,player1_or_player2_list,player1_white,banmen2_out_int): #盤上にその駒より小さい駒がないとFalse
    y=change_za_to_y(zahyo_puted)
    x=change_za_to_x(zahyo_puted)

    for i in range(3):
        koma_kind=7+i #中の大きさを動かそうとしたとき
        koma_kind2=27+i
        if (((banmen2_out_int[y][x]==koma_kind) or (banmen2_out_int[y][x]==koma_kind2)) and (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and
        (10 not in banmen2_out_int[0]) and (10 not in banmen2_out_int[1]) and (10 not in banmen2_out_int[2]) and (10 not in banmen2_out_int[3]) and
        (11 not in banmen2_out_int[0]) and (11 not in banmen2_out_int[1]) and (11 not in banmen2_out_int[2]) and (11 not in banmen2_out_int[3]) and
        (12 not in banmen2_out_int[0]) and (12 not in banmen2_out_int[1]) and (12 not in banmen2_out_int[2]) and (12 not in banmen2_out_int[3]) and
        (30 not in banmen2_out_int[0]) and (30 not in banmen2_out_int[1]) and (30 not in banmen2_out_int[2]) and (30 not in banmen2_out_int[3]) and
        (31 not in banmen2_out_int[0]) and (31 not in banmen2_out_int[1]) and (31 not in banmen2_out_int[2]) and (31 not in banmen2_out_int[3]) and
        (32 not in banmen2_out_int[0]) and (32 not in banmen2_out_int[1]) and (32 not in banmen2_out_int[2]) and (32 not in banmen2_out_int[3])):
            print("その駒は盤面の状況を考えると移動できません")
            return False

    for i in range(3):
        koma_kind=10+i #小の大きさを動かそうとしたとき
        koma_kind2=30+i
        if ((banmen2_out_int[y][x]==koma_kind)or(banmen2_out_int[y][x]==koma_kind2)) and (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]):
            print("その駒は盤面の状況を考えると移動できません")
            return False

    if ((player1_or_player2_list==player1_white and (banmen2_out_int[y][x]>=1 and banmen2_out_int[y][x]<=12)) or
    (player1_or_player2_list==player2_red and (banmen2_out_int[y][x]>=21 and banmen2_out_int[y][x]<=32))):
        return True

    elif banmen2_out_int[y][x]==0:
        print("そこに駒はありません")
        return False

    else:
        print("その駒は動かすことはできません")
        return False
    
def draw_input():
    print("引き分けにするなら、相手と話し合ってhikiwakeと入力してください。そうでないなら、空白のままenterキーを押してください")
    draw=input()
    return draw

def draw_check(draw):
    if draw=="hikiwake" or draw=="":
        return True
    else:
        print("入力が間違っています。もう一度入力してください。")
        print()
        return False

def full_and_small_check(player1_or_player2_list,banmen2_out_int): #外部スタックを盤上に置けない場合True
    if player1_or_player2_list==player1_white:
        for j in range(3): #外部スタックの座標
            for i in range(4):
                if player1_white_outside_stack[j][i]!=0: #その座標にある一番外のスタックのサイズ
                    size1_white=player1_white_outside_stack[j][i]
                    for l in range(3): #プレイヤー１の外部スタックが小サイズかつ満タンの時
                        size_small=10+l
                        if (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and size1_white==size_small:
                            return True

                    for l in range(3): #プレイヤー１の外部スタックが中サイズかつ盤上に相手または自分の駒の小サイズがない場合
                        size_middle=7+l
                        for k in range(10,13,1): #player1の小サイズ
                            if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                            (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and size1_white==size_middle):
                                return True

                        for k in range(30,33,1): #player2の駒の小サイズ
                            if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                            (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and size1_white==size_middle):
                                return True

    if player1_or_player2_list==player2_red:
        for j in range(3): #外部スタックの座標
            for i in range(4):
                if player2_red_outside_stack[j][i]!=0: #その座標にある一番外のスタックのサイズ
                    size1_red=player2_red_outside_stack[j][i]
                    for l in range(3): #プレイヤー2の外部スタックが小サイズかつ満タンの時
                        size_small=30+l
                        if (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and size1_red==size_small:
                            return True

                    for l in range(3): #プレイヤー2の外部スタックが中サイズかつ盤上に相手または自分の駒の小サイズがない場合
                        size_middle=7+l
                        for k in range(10,13,1): #player1の駒の小が盤面にない
                            if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                            (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and size1_red==size_middle):
                                return True

                        for k in range(30,33,1): #player2の駒の小が盤面にない
                            if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                            (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and size1_red==size_middle):
                                return True

    else:
        return False

def stack_zahyo_input():
    check_input=False
    while check_input==False:
        zahyo=input("移動したい外部スタックが置かれている座標を入力してください。(0～2)")
        if zahyo=="0" or zahyo=="1" or zahyo=="2":
            check_input=True
        else:
            print("入力が間違っています。")

    return zahyo

def can_put_judge_take(player1_or_player2_list,koma_size,banmen2_out_int): #入力した座標のスタックより小さいスタックが盤上にあるか
    if (0 in banmen2_out_int[0]) or (0 in banmen2_out_int[1]) or (0 in banmen2_out_int[2]) or (0 in banmen2_out_int[3]):
        return True

    if player1_or_player2_list==player1_white:
        for l in range(3): #プレイヤー１の外部スタックが小サイズかつ満タンの時
            size_small=10+l
            if (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size_small:
                return True

        for l in range(3): #プレイヤー１の外部スタックが中サイズかつ盤上に相手または自分の駒の小サイズがない場合
            size_middle=7+l
            for k in range(10,13,1): #player1の小サイズ
                if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size_middle):
                    return True

            for k in range(30,33,1): #player2の駒の小サイズ
                if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size_middle):
                    return True

    if player1_or_player2_list==player2_red:
        for l in range(3): #プレイヤー2の外部スタックが小サイズかつ満タンの時
            size_small=30+l
            if (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size_small:
                return True
        for l in range(3): #プレイヤー2の外部スタックが中サイズかつ盤上に相手または自分の駒の小サイズがない場合
            size_middle=7+l
            for k in range(10,13,1): #player1の駒の小が盤面にない
                if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size_middle):
                    return True
            for k in range(30,33,1): #player2の駒の小が盤面にない
                if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and
                (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size_middle):
                    return True

    else:
        return False



    if (0 in banmen2_out_int[0]) or (0 in banmen2_out_int[1]) or (0 in banmen2_out_int[2]) or (0 in banmen2_out_int[3]):
        return True

    for i in range(3): #koma_sizeがプレイヤー１の小サイズ
        size_small=10+i
        if koma_size==size_small:
            return False
    
    for j in range(3): #プレイヤー２の小サイズ
        size2_small=30+j
        if koma_size==size2_small:
            return False
    
    for i in range(3): #koma_sizeがプレイヤー１の中サイズかつ満タンで、盤上に相手の駒の小がないとき
        size_middle=7+i
        for k in range(10,13,1): #player1の駒
            if ((k not in banmen2_out_int[0]) and (k not in banmen2_out_int[1]) and (k not in banmen2_out_int[2]) and (k not in banmen2_out_int[3]) and koma_size==size_middle):
                return False

        for l in range(30,33,1): #koma_sizeがプレイヤー１の中サイズかつ満タンで、盤上に自分の駒の小がないとき
            if ((l not in banmen2_out_int[0]) and (l not in banmen2_out_int[1]) and (l not in banmen2_out_int[2]) and (l not in banmen2_out_int[3]) and koma_size==size_middle):
                return False
          
    for j in range(3):
        size2_middle=27+j
        for m in range(10,13,1): #koma_sizeがプレイヤー１の中サイズかつ、盤上に相手の駒の中か小がないとき
            if ((m not in banmen2_out_int[0]) and (m not in banmen2_out_int[1]) and (m not in banmen2_out_int[2]) and (m not in banmen2_out_int[3]) and
            (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size2_middle):
                return False

        for n in range(30,33,1): #koma_sizeがプレイヤー１の中サイズかつ、盤上に自分の駒の中か小がないとき
            if ((n not in banmen2_out_int[0]) and (n not in banmen2_out_int[1]) and (n not in banmen2_out_int[2]) and (n not in banmen2_out_int[3]) and
            (0 not in banmen2_out_int[0]) and (0 not in banmen2_out_int[1]) and (0 not in banmen2_out_int[2]) and (0 not in banmen2_out_int[3]) and koma_size==size2_middle):
                return False

    return True

def form_outside_character(player1_white_outside_stack,player2_red_outside_stack,player1_or_player2_list):
    RED = '\033[31m'
    END = '\033[0m'
    a=RED+"特"+END
    b=RED+"大"+END
    c=RED+"中"+END
    d=RED+"小"+END

    if player1_or_player2_list==player1_white:
        for j in range(3): #外部スタックの座標
            for i in range(4):
                if player1_white_outside_stack[j][i]!=0: #その座標にある一番外のスタックのサイズ
                    size1_white=player1_white_outside_stack[j][i]
                    if size1_white==1 or size1_white==2 or size1_white==3:
                        outside_stack_character[j]="特"
                        break
                    if size1_white==4 or size1_white==5 or size1_white==6:
                        outside_stack_character[j]="大"
                        break
                    if size1_white==7 or size1_white==8 or size1_white==9:
                        outside_stack_character[j]="中"
                        break
                    if size1_white==10 or size1_white==11 or size1_white==12:
                        outside_stack_character[j]="小"
                        break
            if player1_white_outside_stack[j][3]==0:
                outside_stack_character[j]="-"

        return outside_stack_character

    if player1_or_player2_list==player2_red:
        for j in range(3): #外部スタックの座標
            for i in range(4):
                if player2_red_outside_stack[j][i]!=0: #その座標にある一番外のスタックのサイズ
                    size2_red=player2_red_outside_stack[j][i]
                    if size2_red==21 or size2_red==22 or size2_red==23:
                        outside_stack_character[j]=a
                        break
                    if size2_red==24 or size2_red==25 or size2_red==26:
                        outside_stack_character[j]=b
                        break
                    if size2_red==27 or size2_red==28 or size2_red==29:
                        outside_stack_character[j]=c
                        break
                    if size2_red==30 or size2_red==31 or size2_red==32:
                        outside_stack_character[j]=d
                        break
            if player2_red_outside_stack[j][3]==0:
                outside_stack_character[j]="-"
                    
        return outside_stack_character

def check_choise_number(choise_number,player1_or_player2_list):
    if player1_or_player2_list==player1_white:
        if player1_white_outside_stack[choise_number][3]==0:
            print("その場所にはスタックは存在しません")
            return False
        return True

    else:
        if player2_red_outside_stack[choise_number][3]==0:
            print("その場所にはスタックは存在しません")
            return False
        return True

def print_banmen_zahyo():
    print("盤面の座標")
    for i in range(4): #面座標出力
        for j in range(4):
            if banmen_zahyo[i][j]<=9:
                print("",str(banmen_zahyo[i][j])+"|",end="")
            if banmen_zahyo[i][j]>=10:
                print(str(banmen_zahyo[i][j])+"|",end="")
        print()
        for k in range(4):
            print("---",end="")
        print()
    print()

def print_banmen_condition(banmen2_out_character):
    print("盤面の状態")
    print()
    banmen2_out_character=men2_change_character(banmen2_out_int,banmen2_out_character)
    for i in range(4): #面の状態出力
        for j in range(4):
            print(banmen2_out_character[i][j]+"|",end="")
        print()
        for k in range(4):
            print("---",end="")
        print()
    print()

def print_outside_condition():
    ##外部スタックの状態を出力
    print("外部スタックの状態")
    print("---------")
    for i in range(3): #座標表示
        print(str(i),"|",end="")
    print()
    print("---------")
    for i in range(3): #外部スタックの状態
        print(outside_stack_character[i]+"|",end="")
    print()
    print("---------")
    print()


if __name__ == '__main__':

    player1_white=[1,2,3,4,5,6,7,8,9,10,11,12]
    player2_red=[21,22,23,24,25,26,27,28,29,30,31,32]
    banmen_zahyo=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    banmen1_pile=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    banmen2_out_int=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    banmen2_out_character=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    player1_white_outside_stack=[[1,4,7,10],[2,5,8,11],[3,6,9,12]]
    player2_red_outside_stack=[[21,24,27,30],[22,25,28,31],[23,26,29,32]]
    outside_stack_character=["","",""]

    player_change_basic_count=0
    white_coma_kind_basic_count=0
    red_coma_kind_basic_count=0
    full_and_small=False
    koma_size=0
    decrease_basic_number0_white=0
    decrease_basic_number1_white=0
    decrease_basic_number2_white=0
    decrease_basic_number0_red=0
    decrease_basic_number1_red=0
    decrease_basic_number2_red=0

    winer=False
    while winer==False:
        player_change_basic_count+=1 #奇数の時プレイヤー赤
        player1_or_player2_list=player_change(player1_white,player2_red,player_change_basic_count)

        print_banmen_zahyo()    
        print_banmen_condition(banmen2_out_character)
        outside_stack_character=form_outside_character(player1_white_outside_stack,player2_red_outside_stack,player1_or_player2_list)
        print_outside_condition()

        winer=win_check(player2_red,player1_white,banmen2_out_int)
        if winer==True:
            winer_name=winer_which(banmen2_out_int)
            print()
            print(winer_name+"win")
            break

        else:
            draw_input_judge=False
            while draw_input_judge==False:
                draw=draw_input()
                draw_input_judge=draw_check(draw)
            if draw=="hikiwake":
                print("引き分けになりました。ゲームを終了します。")
                break

            player_name_character=player_judge_name(player_change_basic_count)
            print()
            print("今の操作プレイヤーの色："+player_name_character)
            print()
            series=series_check(player1_or_player2_list,player1_white,banmen2_out_int)
            #盤上に自分の駒があるか判定
            exist=exist_check(player_change_basic_count)
            bord_true_or_outside_false=hear_bord_true_or_outside_false(player1_or_player2_list,series,full_and_small,exist)

            #盤面上の駒を操作
            if bord_true_or_outside_false==True:
                put_judge=False
                while put_judge==False:
                    can_move=False
                    while can_move==False:
                        zahyo_puted=int(zahyo_move_input())
                        can_move=can_move_judge(zahyo_puted,player1_or_player2_list,player1_white,banmen2_out_int)
                    coma_kind_int=int(coma_kind_check(banmen2_out_int,zahyo_puted))
                    zahyo=int(zahyo_input())
                    put_judge=can_put_judge_ban(zahyo,coma_kind_int,banmen2_out_int)

                banmen1_pile=men_change(zahyo,coma_kind_int,zahyo_puted)
                banmen2_out_int=banmen2_form(banmen1_pile)
                full_and_small=full_and_small_check(player1_or_player2_list,banmen2_out_int)
                continue
            
            #外部スタックを操作
            elif bord_true_or_outside_false==False:
                if player1_or_player2_list==player1_white:
                    white_coma_kind_basic_count+=1
                else:
                    red_coma_kind_basic_count+=1

                ##自分の外部スタックを選択させる
                check_result=False
                while check_result==False:
                    choise_number_checked=False
                    while choise_number_checked==False:
                        choise_number=int(stack_zahyo_input())
                        print()
                        choise_number_checked=check_choise_number(choise_number,player1_or_player2_list)
                    koma_size=coma_size_decide(player1_or_player2_list,choise_number)
                    check_result=can_put_judge_take(player1_or_player2_list,koma_size,banmen2_out_int)
                put_judge_out=False
                #置く座標を入力
                while put_judge_out==False:
                    zahyo=int(zahyo_input())
                    put_judge_out=can_put_judge_out(series,zahyo,koma_size,banmen2_out_int)
                zahyo_puted=0

                #盤面の状態を変更
                banmen1_pile=men_change(zahyo,koma_size,zahyo_puted)
                banmen2_out_int=banmen2_form(banmen1_pile)
                full_and_small=full_and_small_check(player1_or_player2_list,banmen2_out_int)

                #外部スタックの状態を変更
                if player1_or_player2_list==player1_white:
                    if choise_number==0:
                        decrease_basic_number0_white+=1
                        player1_white_outside_stack[choise_number][decrease_basic_number0_white-1]=0
                    elif choise_number==1:
                        decrease_basic_number1_white+=1
                        player1_white_outside_stack[choise_number][decrease_basic_number1_white-1]=0
                    elif choise_number==2:
                        decrease_basic_number2_white+=1
                        player1_white_outside_stack[choise_number][decrease_basic_number2_white-1]=0

                else:
                    if choise_number==0:
                        decrease_basic_number0_red+=1
                        player2_red_outside_stack[choise_number][decrease_basic_number0_red-1]=0
                    elif choise_number==1:
                        decrease_basic_number1_red+=1
                        player2_red_outside_stack[choise_number][decrease_basic_number1_red-1]=0
                    elif choise_number==2:
                        decrease_basic_number2_red+=1
                        player2_red_outside_stack[choise_number][decrease_basic_number2_red-1]=0