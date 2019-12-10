from flask_wtf import FlaskForm
from wtforms import SubmitField

class GameForm(FlaskForm):
    btn_hit = SubmitField('btn_hit')
    btn_split = SubmitField('btn_split')
    btn_player1_hand1 = SubmitField('btn_player1_hand1')
    btn_player1_hand2 = SubmitField('btn_player1_hand2')
    btn_player2_hand1 = SubmitField('btn_player2_hand1')
    btn_player2_hand2 = SubmitField('btn_player2_hand2')
