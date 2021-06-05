def savedata(gerenciador, usuarios, senhaLogin, validation):
    try:
       opc = str(input('Deseja salvar as alterações feitas? [S/N]: ').upper())
       while opc != 'S' and opc != 'N':
           print('Opção inválida!')
           opc = str(input('Deseja salvar as alterações feitas? [S/N]: ').upper())
    except:
        print('Opção inválida!')
    else:
        if opc == 'S':
            with open('Data_Base_K.txt', 'w') as DataBaseK:
                for k, v in gerenciador.items():
                    DataBaseK.write(f'{k}\n')
                DataBaseK.close()
                pyAesCrypt.encryptFile("Data_Base_K.txt", "Data_Base_K.txt.aes", secury, bufferSize)
                remove('Data_Base_K.txt')
            with open('Data_Base_V.txt', 'w') as DataBaseV:
                for k, v in gerenciador.items():
                    DataBaseV.write(f'{v}\n')
                DataBaseV.close()
                pyAesCrypt.encryptFile("Data_Base_V.txt", "Data_Base_V.txt.aes", secury, bufferSize)
                remove('Data_Base_V.txt')
            print('')
            print('ALTERAÇÕES SALVAS COM SUCESSO! =D')
            print('')
        else:
            print('')
            print('AS ALTERAÇÕES FORAM DESCARTADAS! ;).')
            print('')
    if len(usuarios) != len(validation):
        with open('Log_User.txt', 'w') as DataUser:
            for u in range(len(usuarios)):
                DataUser.write(f'{usuarios[u]}\n')
            DataUser.close()
            pyAesCrypt.encryptFile("Log_User.txt", "Log_User.txt.aes", secury, bufferSize)
            remove('Log_User.txt')
        with open('Log_Password.txt', 'w') as DataPassword:
            for s in range(len(senhaLogin)):
                DataPassword.write(f'{senhaLogin[s]}\n')
            DataPassword.close()
            pyAesCrypt.encryptFile("Log_Password.txt", "Log_Password.txt.aes", secury, bufferSize)
            remove('Log_Password.txt')