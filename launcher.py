from src.api.app.main_component import MainComponent

main_component = MainComponent()

if __name__ == '__main__':
    main_component.start_server()
    main_component.delete()
