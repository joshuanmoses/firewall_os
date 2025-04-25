from services import firewall_service, vlan_service, ids_service
import threading

def main():
    t1 = threading.Thread(target=firewall_service.run)
    t2 = threading.Thread(target=vlan_service.run)
    t3 = threading.Thread(target=ids_service.run)
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
