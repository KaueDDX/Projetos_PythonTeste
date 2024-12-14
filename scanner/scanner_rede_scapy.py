import scapy.all as scapy

def escanear_rede(endereco):
    scapy.arping(endereco)

escanear_rede("172.16.20.53")