# devopstsm

## ОБРАТИЛ ВНИМАНИЯ ЧТО НЕ СДАЛ ДЗ ЗА 8 УРОК

1) Посчитайте диапазон доступных IP - адресов
хостов, а также адрес широковещательного
запроса для подсети 10.1.1.0 с битовыми
масками:
1) /28 - min(10.1.1.1) max(10.1.1.14)  Broadcast(10.1.1.15)
2) /30 - min(10.1.1.1) max(10.1.1.2)  Broadcast(10.1.1.3)
3) /25 - min(10.1.1.1) max(10.1.1.126) Broadcast(10.1.1.127)

2) Добиться получения ip адреса из под сети
169.254.х.х, можно ли использовать подобную
адресацию и построить на этом сеть? 

Это зарезервированный адрес подсети, который задается автоматически, если не получается подключится по  DHCP

3) Что такое адреса apipa?

Служба Automatic Private IP Addressing (APIPA) позволяет клиентам DHCP автоматически настраивать IP-адрес и маску подсети, когда недоступен сервер DHCP. 
Устройству назначается IP-адрес в диапазоне от 169.254.1.0 до 169.254.254.255.
Маске подсети автоматически присваивается значение 255.255.0.0, а шлюзу - 0.0.0.0.


4) Составить список зарезервированных
подсетей

   0.0.0.0/8            "This" Network                 [RFC1700, page 4]
   10.0.0.0/8           Private-Use Networks                   [RFC1918]
   14.0.0.0/8           Public-Data Networks         [RFC1700, page 181]
   24.0.0.0/8           Cable Television Networks                    --
   39.0.0.0/8           Reserved but subject
                           to allocation                       [RFC1797]
   127.0.0.0/8          Loopback                       [RFC1700, page 5]
   128.0.0.0/16         Reserved but subject
                           to allocation                             --
   169.254.0.0/16       Link Local                                   --
   172.16.0.0/12        Private-Use Networks                   [RFC1918]
   191.255.0.0/16       Reserved but subject
                           to allocation                             --
   192.0.0.0/24         Reserved but subject
                           to allocation                             --
   192.0.2.0/24         Test-Net
   192.88.99.0/24       6to4 Relay Anycast                     [RFC3068]
   192.168.0.0/16       Private-Use Networks                   [RFC1918]
   198.18.0.0/15        Network Interconnect
                           Device Benchmark Testing            [RFC2544]
   223.255.255.0/24     Reserved but subject
                           to allocation                             --
   224.0.0.0/4          Multicast                              [RFC3171]
   240.0.0.0/4          Reserved for Future Use        [RFC1700, page 4]
