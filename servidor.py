from rpc.servidores.Server import Server


def main():
    server = Server('localhost', 45000)
    server.iniciar()



if __name__ == '__main__':
    main()