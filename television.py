class Television:
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL=3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        method to power on/off remote
        """
        if self.__status:
            if self.__status == False:
                self.__status = True
            else:
                self.__status = False

    def mute(self) -> None:
        """
        method to mute and unmute remote
        """
        if self.__muted:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        """
        method to increase the tv channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    def channel_down(self):
        """
        method to decrease the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def volume_up(self):
        """
        method to increase volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        method to decrease volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self) -> str:
        """
        Method to show the tv status
        :return: tv status
        """
        if self.__muted == True:
            return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = (0)'
        return f'Power = [{self.__status}], Channel = [{self.__channel}, Volume = [{self.__volume}]'