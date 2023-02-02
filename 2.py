""""Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)"""

class XOgame():
    def __init__(self) -> None:
        import random
        self.rand = random
        self.my_field = [[0 for _ in range(3)] for _ in range(3)]
        self.coord_list = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        self.current_player = 0
        self.human_player = 0
        self.bot_player = 0
        self.game_type = 0 
        self.player_dict = {1:'X', -1:'O'}
        
    def PrintField(self):
        names_field = [['  _1__2__3_ '], ['a|', 'b|', 'c|']]
        print(names_field[0][0])
        for i, elem in enumerate(self.my_field):
            print(names_field[1][i], end='')
            for ii, x in enumerate(elem):
                if x==0:
                    print(' _ ', end='')
                elif x==-1:
                    print(' O ', end='')
                elif x==1:
                    print(' X ', end='')
                else:
                    print(f' {x} ', end='')
                
                if ii == 2:
                    print('|')
        print('  _________ ')

    def ChangeValue(self, coord='a1', value=1) -> bool:
        coord_dict = {'a':0, 'b':1, 'c':2, '1':0, '2':1, '3':2}
        y,x = coord
        
        if self.my_field[coord_dict[y]][coord_dict[x]]==0:
            self.my_field[coord_dict[y]][coord_dict[x]] = value
            return True
        return False

    def CheckWin(self) -> str:
        '''проверка поля на выигрыш или окончание игры'''
        winer = 0
        
        for i in range(3):
            if (sum(self.my_field[i])==-3):
                winer = -3 
            elif (sum(self.my_field[i])==3):
                winer = 3
        
        
        verticals = [0 for _ in range(3)]
        for i in range(3):
            for ii in range(3):
                verticals[ii] += self.my_field[i][ii]
        if (-3 in verticals):
            winer = -3 
        elif (3 in verticals):
            winer = 3
            
        crosses = [0,0]
        crosses[0] = self.my_field[0][0] + self.my_field[1][1] + self.my_field[2][2]
        crosses[1] = self.my_field[0][2] + self.my_field[1][1] + self.my_field[2][0]
        if (-3 in crosses):
            winer = -3 
        elif (3 in crosses):
            winer = 3

        
        if ( winer == 3 * self.human_player ):
            print('gg ez') 
            return True
        elif ( winer == 3 * self.bot_player):
            print('ggwp lose')
            return True

        
        is_filled = 0
        for i in range(3):
            for ii in range(3):
                if self.my_field[i][ii] != 0:
                    is_filled += 1
        if is_filled == 9:
            print('End Game!')
            return True

        return False
    
    def PlayersDefine(self):
        while self.current_player not in [-1,1]:
            self.current_player = int(input('Введите, чем будете играть? O:-1 X:1 '))
        self.human_player = self.current_player
        print(f'Вы будете играть {self.player_dict[self.current_player]}')
        self.bot_player = -self.current_player
        print(f'Ваш противник будет играть {self.player_dict[self.bot_player]}')

    def PlayerTurn(self, change_player=False):
        coord = 'xx'
        
        if change_player:
            if self.current_player == -1:
                self.current_player = 1
            else:
                self.current_player = -1

        if (self.current_player == self.bot_player) and (self.game_type == 1):
            
            self.BotTurn()
            return True
        while coord not in self.coord_list:
            coord = input(f'Введите кординату для {self.player_dict[self.current_player]} или q чтоб покинуть: ')
            if coord == 'q':
                print('Quit!')
                return False

        self.ChangeValue(coord=coord, value=self.current_player)
        self.PrintField()
        return True

    def BotTurn(self):
        while True:
            for i in range(3):
                for ii in range(3):
                    if self.my_field[i][ii] == 0:
                        if self.rand.randint(0,9) == 1:
                            self.my_field[i][ii] = self.bot_player
                            print('Бот походил:')
                            self.PrintField()
                            return True
                        else:
                            continue
        






    def GameStart(self):
        print('Играем на поле:')
        self.game_type = int(input('Выберите тип игры: 0 - игра с другом, 1 - игра с ботом: '))
        self.PrintField()
        self.PlayersDefine()
        self.PlayerTurn()
        while True:
            if not self.PlayerTurn(change_player=True):
                return
            if self.CheckWin():
                print('END Game')
                return
        
        


my_game = XOgame()
my_game.GameStart()