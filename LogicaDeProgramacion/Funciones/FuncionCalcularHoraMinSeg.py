def convertiHoraMinSeg(seg): #seg=3624
    ''' Retora la hora, min y segundos que representa la cantidad de segundos que recibe.'''
    
    ''' 60*60 - Da la cantidad de segundos en una hora se divide por los segundos que ingresan
       por teclado y obtengo la cantidad de horas '''
    
    hora = seg // (60*60)         # 1 hora y sobran 24segundos   <- Esto retorno
    seg = seg%(60*60)             # Sobran 24 '''
    minutos = seg // 60           # 0                                                     <- Esto retorno
    seg = seg % 60                    # los segundos que sobran          <- Esto retorno 
    
    return hora, minutos, seg