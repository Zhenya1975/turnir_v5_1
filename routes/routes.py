
from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for, abort
from sqlalchemy import desc
# from ..models.models import ParticipantsDB, FightsDB, CompetitionsDB, BacklogDB, RegistrationsDB
from extensions.extensions import db, migrate
import csv

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
def home_view():
    return "home"