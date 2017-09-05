from nanogateway import NanoGateway

if __name__ == '__main__':
    # Gateway configuration. Change as you need.
    GW = NanoGateway(
        wifi_ssid='My Awesome Network',
        wifi_password='super-secret'
    )

    GW.start()
    GW.log('You may now press ENTER to open a REPL.')
    input()
