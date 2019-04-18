import ntplib


class NTPPerformance:
    """

    """
    ntp_servers = [
                    "ntp3.stratum1.ru",
                    "ntp1.stratum1.ru",
                    "ntp2.stratum1.ru",
                    "ntp5.stratum2.ru",
                    "ntp2.stratum2.ru",
                    "ntp4.stratum2.ru",
                    "ntp3.stratum2.ru",
                    "ntp1.stratum2.ru",
                    "europe.pool.ntp.org",
                    "ntp4.stratum1.ru",
                    "ntp5.stratum1.ru",
                ]

    def __init__(self):
        self.__Connection = ntplib.NTPClient()

    def get_utc(self):
        for ntp_name in self.ntp_servers:
            try:
                resp = self.__Connection.request(ntp_name, version=3)
                return resp.tx_time
            except ntplib.NTPException:
                continue
            except Exception:
                continue
        return None


if __name__ == '__main__':
    ntp = NTPPerformance()
    print(ntp.get_utc())
