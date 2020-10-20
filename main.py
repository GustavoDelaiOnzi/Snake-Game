import pygame
from random import randint

def desenharGrade(grade, tela):
    flag = 0
    verdeEscuro = (170, 215, 81)
    verdeClaro = (162, 209, 73)
    for bloco in grade:
        if flag == 0:
            pygame.draw.rect(tela, verdeEscuro, [bloco[0]*50, bloco[1]*50, 50, 50])
            flag += 1
        else:
            pygame.draw.rect(tela, verdeClaro, [bloco[0]*50, bloco[1]*50, 50, 50])
            flag -= 1

def desenharCobra(cobra, tela):
    for bloco in cobra:
        if bloco != cobra[-1] and bloco[0] == cobra[cobra.index(bloco) + 1][0] and bloco[1] < cobra[cobra.index(bloco) + 1][1]:
            pygame.draw.rect(tela, (30, 80, 215), (bloco[0]*50+5, bloco[1]*50+5, 40, 50))
        elif bloco != cobra[-1] and bloco[0] == cobra[cobra.index(bloco) + 1][0] and bloco[1] > cobra[cobra.index(bloco) + 1][1]:
            pygame.draw.rect(tela, (30, 80, 215), (bloco[0]*50+5, bloco[1]*50-5, 40, 50))
        elif bloco != cobra[-1] and bloco[1] == cobra[cobra.index(bloco) + 1][1] and bloco[0] < cobra[cobra.index(bloco) + 1][0]:
            pygame.draw.rect(tela, (30, 80, 215), (bloco[0]*50+5, bloco[1] * 50+5, 50, 40))
        elif bloco != cobra[-1] and bloco[1] == cobra[cobra.index(bloco) + 1][1] and bloco[0] > cobra[cobra.index(bloco) + 1][0]:
            pygame.draw.rect(tela, (30, 80, 215), (bloco[0]*50-5, bloco[1] * 50+5, 50, 40))
    pygame.draw.rect(tela, (60, 10, 150), (cobra[-1][0]*50+5, cobra[-1][1]*50+5, 40, 40))

def main():
    pygame.init()
    tela = pygame.display.set_mode((850, 750))
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    azul = (30, 80, 215)

    timer = 0
    score = 0
    direcao = "right"
    clock = pygame.time.Clock()

    cobra = [[2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8]]
    listaDeMovimentos = []
    blocosLivres = []
    start = True
    gameover = False
    recorde = 0
    myfont = pygame.font.SysFont('Impact', 25)

    grade = []

    for y in range(0, 15):
        for x in range(0, 17):
            grade.append([x, y])
            blocosLivres.append([x, y])
    for bloco in cobra:
        blocosLivres.remove(bloco)
    maca = blocosLivres[randint(0, len(blocosLivres) - 1)]

    SAIR_DO_JOGO = False
    while not SAIR_DO_JOGO:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SAIR_DO_JOGO = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if len(listaDeMovimentos) < 2:
                        listaDeMovimentos.append("right")
                if event.key == pygame.K_LEFT :
                    if len(listaDeMovimentos) < 2:
                        listaDeMovimentos.append("left")
                if event.key == pygame.K_UP :
                    if len(listaDeMovimentos) < 2:
                        listaDeMovimentos.append("up")
                if event.key == pygame.K_DOWN :
                    if len(listaDeMovimentos) < 2:
                        listaDeMovimentos.append("down")
        desenharGrade(grade, tela)
        desenharCobra(cobra, tela)
        if timer > 12:
            timer = 0
            if len(listaDeMovimentos) == 0:
                listaDeMovimentos.append(direcao)
            if listaDeMovimentos[0] == "right" and direcao == "left":
                listaDeMovimentos[0] = "left"
            elif listaDeMovimentos[0] == "left" and direcao == "right":
                listaDeMovimentos[0] = "right"
            elif listaDeMovimentos[0] == "up" and direcao == "down":
                listaDeMovimentos[0] = "down"
            elif listaDeMovimentos[0] == "down" and direcao == "up":
                listaDeMovimentos[0] = "up"
            
            if listaDeMovimentos[0] == "right":
                direcao = "right"
                cobra.append([cobra[-1][0]+1, cobra[-1][1]])
            elif listaDeMovimentos[0] == "up":
                direcao = "up"
                cobra.append([cobra[-1][0], cobra[-1][1]-1])
            elif listaDeMovimentos[0] == "left":
                direcao = "left"
                cobra.append([cobra[-1][0]-1, cobra[-1][1]])
            elif listaDeMovimentos[0] == "down":
                direcao = "down"
                cobra.append([cobra[-1][0], cobra[-1][1]+1])
        
            blocosLivres.append(cobra[0])
            try:
                blocosLivres.remove(cobra[-1])
            except:
                pass
            try:
                del listaDeMovimentos[0]
            except:
                pass
            if cobra[-1] == maca:
                maca = blocosLivres[randint(0, len(blocosLivres) - 1)]
                score += 1
            else:
                del cobra[0]
        
        if cobra[-1][0] > 16 or cobra[-1][1] > 14 or cobra[-1][0] < 0 or cobra[-1][1] < 0:
            gameover = True
            if score > recorde:
                recorde = score
            start = True

        for i in range(0, len(cobra)-2):
            if cobra[-1] == cobra[i]:
                gameover = True
                if score > recorde:
                    recorde = score
                start = True

        pygame.draw.rect(tela, (180, 10, 0), (maca[0]*50+5, maca[1]*50+5, 40, 40))
        scoretxt = myfont.render("Score: " + str(score), 20, (255, 0, 0))
        tela.blit(scoretxt, (0, 0))
        timer += 1
        clock.tick(60)


        while start:
            pygame.draw.rect(tela, (255, 255, 255), (850 / 2 - 200, 700 / 2 - 100, 400, 200))
            pygame.draw.rect(tela, (0, 0, 0), (850/2-75, 750/2-25+20, 150, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    SAIR_DO_JOGO = True
            if pygame.mouse.get_pressed()[0] == True:
                if pygame.mouse.get_pos()[0] > 850/2-75 and pygame.mouse.get_pos()[0] < 850/2-75+150:
                    if pygame.mouse.get_pos()[1] > 750/2-25+20 and pygame.mouse.get_pos()[1] < 750/2-25+50+20:
                        start = False
                        score = 0
                        cobra = [[2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8]]
                        livre = []
                        for bloco in grade:
                            livre.append(bloco)
                        for bloco in cobra:
                            livre.remove(bloco)
                        if len(listaDeMovimentos)>0:
                            listaDeMovimentos = ["right"]
                            direcao = "right"
                        else:
                            direcao = "right"
            if not gameover:
                aperte = myfont.render("Aperte para comecar", 20, (255, 0, 0))
                tela.blit(aperte, (850 / 2 - 200+95, 700 / 2 - 100+10))
            else:
                aperte = myfont.render("Jogar novamente?", 20, (255, 0, 0))
                tela.blit(aperte, (850 / 2 - 200+110, 700 / 2 - 100 + 5))
                scoretxt = myfont.render("Score: " + str(score), 20, (255, 0, 0))
                tela.blit(scoretxt, (850 / 2 - 200+10, 700 / 2 - 100+40))
                scoretxt = myfont.render("Recorde: " + str(recorde), 20, (255, 0, 0))
                tela.blit(scoretxt, (850 / 2 - 200 + 10, 700 / 2 - 100 + 70))
            pygame.display.update()
        pygame.display.update()


if __name__ == "__main__":
    main()