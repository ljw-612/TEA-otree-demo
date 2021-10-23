from otree.api import *
import pandas as pd
import time

from io import BytesIO
import base64

import numpy as np
import matplotlib.pyplot as plt
import random

data = pd.read_csv('D:/Duke/Y2/innovative_teaching/otree_demos/prisoner_test/fnq-demo/survey/eth-usd-max.csv')
c = cu

doc = ''
class Constants(BaseConstants):
    US = 100000
    ETH = 200
    players_per_group = 2
    name_in_url = 'survey'
    num_rounds = 1
    pricesDay1_10 = [194.39, 197.78, 196.78, 196.86, 215.55, 206.27, 211.98, 214.15, 210.06, 206.94]

# def after_all_players_arrive1(subsession):
#     session = subsession.session
#     subsession.group_randomly()

def creating_session(subsession):
    subsession.group_randomly()

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    US = models.FloatField(initial=100000, app_name='survey')
    ETH = models.FloatField(initial=200, app_name='survey')
    # Asset_list = []
    ROI = models.FloatField(initial=None, app_name='survey')
    ROI2 = models.FloatField(initial=None, app_name='survey')
    ROI3 = models.FloatField(initial=None, app_name='survey')

    US2 = models.FloatField(initial=100000, app_name='survey')
    ETH2 = models.FloatField(initial=200, app_name='survey')
    Asset_day1 = models.FloatField(initial=None, app_name='survey')
    Asset_day10 = models.FloatField(initial=None, app_name='survey')
    value_total_asset = models.FloatField(initial=0, app_name='survey')

    Name = models.StringField(label="Your Name")
    Sig = models.StringField(label="Your Signature")
    Email = models.StringField(label="Your Email Address")
    Date = models.StringField(label="Date")

    one = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='1) I usually get what I want in life.  ',
                             widget=widgets.RadioSelect)
    two = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='2) I need to be kept informed about news events.',
                             widget=widgets.RadioSelect)
    three = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='3) I never know where I stand with other people.',
                             widget=widgets.RadioSelect)
    four = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='4) I do not really believe in luck or chance. ',
                             widget=widgets.RadioSelect)
    five = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='5) I think that I could easily win a lottery. ',
                             widget=widgets.RadioSelect)
    six = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='6) If I do not succeed in a task, I tend to give up. ',
                             widget=widgets.RadioSelect)
    seven = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='7) I usually convince others to do things my way. ',
                             widget=widgets.RadioSelect)
    eight = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='8) People make a difference in controlling crime. ',
                             widget=widgets.RadioSelect)
    nine = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='9) The success I have is largely a matter of chance. ',
                             widget=widgets.RadioSelect)
    ten = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='10) Marriage is largely a gamble for most people.  ',
                             widget=widgets.RadioSelect)
    eleven = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='11) People must be the master of their own fate. ',
                             widget=widgets.RadioSelect)
    twelve = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='12) It is not important for me to vote.  ',
                             widget=widgets.RadioSelect)
    thirteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='13) My life seems like a series of random events. ',
                             widget=widgets.RadioSelect)
    fourteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='14) I never try anything that I am not sure of. ',
                             widget=widgets.RadioSelect)
    fifteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='15) I earn the respect and honors I receive. ',
                             widget=widgets.RadioSelect)
    sixteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='16) A person can get rich by taking risks. ',
                                  widget=widgets.RadioSelect)
    seventeen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='17) Leaders are successful when they work hard. ',
                                  widget=widgets.RadioSelect)
    eighteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='18) Persistence and hard work usually lead to success. ',
                                 widget=widgets.RadioSelect)
    nineteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='19) It is difficult to know who my real friends are. ',
                                  widget=widgets.RadioSelect)
    twenty = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='20) Other people usually control my life. ',
                                  widget=widgets.RadioSelect)


    Choice1 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice2 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice3 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice4 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice5 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice6 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice7 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice8 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice9 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice10 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')

    time_choice1 = models.FloatField(initial=None,app_name='survey')
    time_choice2 = models.FloatField(initial=None, app_name='survey')
    time_choice3 = models.FloatField(initial=None, app_name='survey')
    time_choice4 = models.FloatField(initial=None, app_name='survey')
    time_choice5 = models.FloatField(initial=None, app_name='survey')
    time_choice6 = models.FloatField(initial=None, app_name='survey')
    time_choice7 = models.FloatField(initial=None, app_name='survey')
    time_choice8 = models.FloatField(initial=None, app_name='survey')
    time_choice9 = models.FloatField(initial=None, app_name='survey')
    time_choice10 = models.FloatField(initial=None, app_name='survey')


    Choice_2 = models.StringField(choices=[['1','Strategy A'], ['2','Strategy B'],['3','Strategy C']], label='Choose the AI strategy',
                                  widget=widgets.RadioSelect)
    Choice_3 = models.StringField(choices=[['1', 'AI Strategy'], ['2', 'Believe yourself']],
                                  label='Choose the session 3 decision',
                                  widget=widgets.RadioSelect)

# class ShuffleWaitPage(WaitPage):
#     wait_for_all_groups = False
#     after_all_players_arrive = 'after_all_players_arrive1'

class Consent(Page):
    pass

class PleaseRead(Page):
    form_model = 'player'
    form_fields = ['Name','Sig','Email','Date']

class Psycho(Page):
    form_model = 'player'
    form_fields = ['one','two', 'three', 'four', 'five', 'six', 'seven' ,'eight' ,'nine' ,'ten' ,'eleven' ,'twelve',
                   'thirteen', 'fourteen' ,'fifteen', 'sixteen', 'seventeen','eighteen', 'nineteen', 'twenty']

class Day1(Page):
    form_model = 'player'
    form_fields = ['Choice1']

    @staticmethod
    def vars_for_template(player: Player):

        current_price =  Constants.pricesDay1_10[0]
        player.value_total_asset = player.US + player.ETH * float(current_price)
        player.Asset_day1 = player.value_total_asset
        global time1
        time1 = float(time.time())

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day2(Page):
    form_model = 'player'
    form_fields = ['Choice2']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[0])
        player.US = player.US - player.Choice1 * formal_price
        player.ETH = player.ETH + player.Choice1
        global time2
        time2 = float(time.time())
        player.time_choice1 = time2 - time1

        # 第二天
        current_price =  Constants.pricesDay1_10[1]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day3(Page):
    form_model = 'player'
    form_fields = ['Choice3']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[1])
        player.US = player.US - player.Choice2 * formal_price
        player.ETH = player.ETH + player.Choice2
        global time3
        time3 = float(time.time())
        player.time_choice2 = time3 - time2

        # 第二天
        current_price =  Constants.pricesDay1_10[2]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day4(Page):
    form_model = 'player'
    form_fields = ['Choice4']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[2])
        player.US = player.US - player.Choice3 * formal_price
        player.ETH = player.ETH + player.Choice3
        global time4
        time4 = float(time.time())
        player.time_choice3 = time4 - time3

        # 第二天
        current_price =  Constants.pricesDay1_10[3]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day5(Page):
    form_model = 'player'
    form_fields = ['Choice5']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[3])
        player.US = player.US - player.Choice4 * formal_price
        player.ETH = player.ETH + player.Choice4
        global time5
        time5 = float(time.time())
        player.time_choice4 = time5 - time4

        # 第二天
        current_price =  Constants.pricesDay1_10[4]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day6(Page):
    form_model = 'player'
    form_fields = ['Choice6']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[4])
        player.US = player.US - player.Choice5 * formal_price
        player.ETH = player.ETH + player.Choice5
        global time6
        time6 = float(time.time())
        player.time_choice5 = time6 - time5

        # 第二天
        current_price =  Constants.pricesDay1_10[5]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day7(Page):
    form_model = 'player'
    form_fields = ['Choice7']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[5])
        player.US = player.US - player.Choice6 * formal_price
        player.ETH = player.ETH + player.Choice6
        global time7
        time7 = float(time.time())
        player.time_choice6 = time7 - time6

        # 第二天
        current_price =  Constants.pricesDay1_10[6]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day8(Page):
    form_model = 'player'
    form_fields = ['Choice8']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[6])
        player.US = player.US - player.Choice7 * formal_price
        player.ETH = player.ETH + player.Choice7
        global time8
        time8 = float(time.time())
        player.time_choice7 = time8 - time7

        # 第二天
        current_price =  Constants.pricesDay1_10[7]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day9(Page):
    form_model = 'player'
    form_fields = ['Choice9']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[7])
        player.US = player.US - player.Choice8 * formal_price
        player.ETH = player.ETH + player.Choice8
        global time9
        time9 = float(time.time())
        player.time_choice8 = time9 - time8

        # 第二天
        current_price =  Constants.pricesDay1_10[8]
        player.value_total_asset = player.US + player.ETH * float(current_price)

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

class Day10(Page):
    form_model = 'player'
    form_fields = ['Choice10']
    @staticmethod
    def vars_for_template(player):
        # 前一天
        formal_price = float(Constants.pricesDay1_10[8])
        player.US = player.US - player.Choice9 * formal_price
        player.ETH = player.ETH + player.Choice9
        global time10
        time10 = float(time.time())
        player.time_choice9 = time10 - time9

        # 第二天
        current_price =  Constants.pricesDay1_10[9]
        player.value_total_asset = player.US + player.ETH * float(current_price)
        player.Asset_day10 = player.value_total_asset

        return dict(
            current_price = current_price,
            value_total_asset = player.value_total_asset,
            US = player.US,
            ETH = player.ETH,
        )

# class Summary_phase1(Page):
#     @staticmethod
#     def vars_for_template(player: Player):
#         player.US = player.US - player.Choice10
#         player.ETH = player.ETH + player.Choice10
#         global time11
#         time11 = float(time.time())
#         player.time_choice10 = time11 - time10
#
#
#         ROI = (player.Asset_day10 - player.Asset_day1) / player.Asset_day1
#         player.ROI = ROI
#         return dict(
#             US = player.US,
#             ETH = player.ETH,
#             value_total_asset = player.Asset_day10,
#             ROI = ROI,
#         )

class Session2_Opening(Page):
    form_model = 'player'
    form_fields = ['Choice_2']

    @staticmethod
    def is_displayed(player: Player):
        return int(player.id_in_group) == 1

class Session2_Opening_2(Page):
    form_model = 'player'
    form_fields = ['Choice_2']

    @staticmethod
    def is_displayed(player: Player):
        return int(player.id_in_group) == 2

class Session3_Opening(Page):
    form_model = 'player'
    form_fields = ['Choice_3']
    @staticmethod
    def vars_for_template(player: Player):
        player.US = player.US - player.Choice10
        player.ETH = player.ETH + player.Choice10
        global time11
        time11 = float(time.time())
        player.time_choice10 = time11 - time10

        ROI = (player.Asset_day10 - player.Asset_day1) / player.Asset_day1
        player.ROI = ROI
        choice_2 = player.Choice_2
        ai_choice = choice_2
        # 每天都买
        if ai_choice == '1':
            # price_day1 = float(data.iloc[index]['price'])
            # total_asset_day1 = US2 + price_day1*ETH2
            # prices_for_ten_days = data.iloc[index: index+10]['price'].sum()
            # spent_money = 10 * prices_for_ten_days
            #
            # US2 = US2 - spent_money
            # ETH2 = ETH2 + 100
            #
            # price_day10 = float(data.iloc[index+10]['price'])
            # total_asset_day10 = US2 + price_day10 * ETH2
            # ROI = (total_asset_day10-total_asset_day1) / total_asset_day1
            player.ROI2 = 1
        # 都卖
        elif ai_choice =='2':
            # price_day1 = float(data.iloc[index]['price'])
            # total_asset_day1 = US2 + price_day1*ETH2
            # prices_for_ten_days = data.iloc[index: index+10]['price'].sum()
            # received_money = 10 * prices_for_ten_days
            #
            # US2 = US2 + received_money
            # ETH2 = ETH2 - 100
            #
            # price_day10 = float(data.iloc[index+10]['price'])
            # total_asset_day10 = US2 + price_day10 * ETH2
            # ROI = (total_asset_day10-total_asset_day1) / total_asset_day1
            player.ROI2 =1

        elif ai_choice == '3':
            # price_day1 = float(data.iloc[index]['price'])
            # price_day10 = float(data.iloc[index + 10]['price'])
            # total_asset_day1 = US2 + price_day1 * ETH2
            # total_asset_day10 = US2 + price_day10 * ETH2
            # ROI = (total_asset_day10-total_asset_day1) / total_asset_day1
            player.ROI2 =1

        return dict(
            US=player.US,
            ETH=player.ETH,
            value_total_asset=player.Asset_day10,
            ROI=ROI,
        )


class Endings(Page):
    @staticmethod
    def vars_for_template(player: Player):
        choice_3 = player.Choice_3
        ai_choice = choice_3
        # 每天都买
        if ai_choice == '1':
            player.ROI3 = player.ROI2
        # 都卖
        elif ai_choice =='2':
            player.ROI3 = player.ROI


page_sequence = [Consent, PleaseRead, Psycho, Session2_Opening,
                 Day1, Day2, Day3, Day4, Day5,
                 Day6, Day7, Day8, Day9, Day10,
                 Session2_Opening_2, Session3_Opening, Endings]

# page_sequence = [Day1, Day2]