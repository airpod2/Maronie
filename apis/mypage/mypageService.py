from flask import abort, session
from flask_restx import marshal
from models.liquor import *
from models.paring import *
from models.user import *
from db_connect import db
import pymysql
import os

# 위시리스트 출력
def wishlist(user_id:int):
    # logined_user = User.query.filter_by(email=session['login']).first()

    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    # else:
    liquors = Wishlist_liquor.query.filter_by(user_id = user_id).all()
    cocktails = Wishlist_cocktail.query.filter_by(user_id = user_id).all()
    
    result = {"liquor": liquors, "cocktail":cocktails}

    return result,200

# liquor 위시리스트 추가
def create_wishlist_liquor(user_id:int,liquor_id:int):
    wishlist_check = Wishlist_liquor.query.filter_by(user_id = user_id).filter_by(liquor_id = liquor_id).first()
    if wishlist_check:
        abort(500, "이미 등록된 위시리스트입니다.")
    try:
        new_wishlist = Wishlist_liquor(user_id=user_id,liquor_id=liquor_id)
        db.session.add(new_wishlist)
        db.session.commit()
        return {"message":"위시리스트 등록 성공"},200
    except:
        abort(500, "위시리스트 등록 실패")

# cocktail 위시리스트 추가
def create_wishlist_cocktail(user_id:int,cocktail_id:int):
    wishlist_check = Wishlist_cocktail.query.filter_by(user_id = user_id).filter_by(cocktail_id = cocktail_id).first()
    if wishlist_check:
        abort(500, "이미 등록된 위시리스트입니다.")
    try:
        new_wishlist = Wishlist_cocktail(user_id=user_id,cocktail_id=cocktail_id)
        db.session.add(new_wishlist)
        db.session.commit()
        return {"message":"위시리스트 등록 성공"},200
    except:
        abort(500, "위시리스트 등록 실패")

#술 위시리스트 삭제
def delete_wishlist_liquor(user_id:int, liquor_id:int):
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'),
                           port=int(os.getenv('MYSQL_PORT')),
                           user=os.getenv('MYSQL_USER'), 
                           password=os.getenv('MYSQL_PASSWORD'), 
                           db=os.getenv('MYSQL_DATABASE'), charset='utf8')
    cur = conn.cursor()
    sql= """DELETE from wishlist_liquor WHERE user_id=%s AND liquor_id=%s"""
    try:
        cur.execute(sql,(user_id, liquor_id))
        conn.commit()
        return {"message":"술 위시리스트 삭제 성공"},200
    except: 
        abort(500, "술 위시리스트 삭제 실패")

#칵테일 위시리스트 삭제
def delete_wishlist_cocktail(user_id:int, cocktail_id:int):
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'), 
                           port=int(os.getenv('MYSQL_PORT')), 
                           user=os.getenv('MYSQL_USER'),
                           password=os.getenv('MYSQL_PASSWORD'), 
                           db=os.getenv('MYSQL_DATABASE'), charset='utf8')
    cur = conn.cursor()
    sql= """DELETE from wishlist_cocktail WHERE user_id=%s AND cocktail_id=%s"""
    try:
        cur.execute(sql,(user_id, cocktail_id))
        conn.commit()
        return {"message":"술 위시리스트 삭제 성공"},200
    except: 
        abort(500, "술 위시리스트 삭제 실패")


# donelist 출력
def donelist(user_id:int):
    # logined_user = User.query.filter_by(email=session['login']).first()

    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    # else:
    liquors = Donelist_liquor.query.filter_by(user_id = user_id).all()
    cocktails = Donelist_cocktail.query.filter_by(user_id = user_id).all()
    
    result = {"liquor": liquors, "cocktail":cocktails}

    return result,200

# liquor donelist 추가
def create_donelist_liquor(user_id:int,liquor_id:int):
    donelist_check = Donelist_liquor.query.filter_by(user_id = user_id).filter_by(liquor_id = liquor_id).first()
    if donelist_check:
        abort(500, "이미 등록된 donelist입니다.")
    try:
        new_donelist = Donelist_liquor(user_id=user_id,liquor_id=liquor_id)
        db.session.add(new_donelist)
        db.session.commit()
        return {"message":"donelist 등록 성공"},200
    except:
        abort(500, "donelist 등록 실패")

# cocktail donelist 추가
def create_donelist_cocktail(user_id:int,cocktail_id:int):
    donelist_check = Donelist_cocktail.query.filter_by(user_id = user_id).filter_by(cocktail_id = cocktail_id).first()
    if donelist_check:
        abort(500, "이미 등록된 donelist입니다.")
    try:
        new_donelist = Donelist_cocktail(user_id=user_id,cocktail_id=cocktail_id)
        db.session.add(new_donelist)
        db.session.commit()
        return {"message":"donelist 등록 성공"},200
    except:
        abort(500, "donelist 등록 실패")

#술 donelist 삭제
def delete_donelist_liquor(user_id:int, liquor_id:int):
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'), 
                           port=int(os.getenv('MYSQL_PORT')), 
                           user=os.getenv('MYSQL_USER'),
                           password=os.getenv('MYSQL_PASSWORD'), 
                           db=os.getenv('MYSQL_DATABASE'), charset='utf8')
    cur = conn.cursor()
    sql= """DELETE from donelist_liquor WHERE user_id=%s AND liquor_id=%s"""
    try:
        cur.execute(sql,(user_id, liquor_id))
        conn.commit()
        return {"message":"술 donelist 삭제 성공"},200
    except: 
        abort(500, "술 donelist 삭제 실패")

#칵테일 donelist 삭제
def delete_donelist_cocktail(user_id:int, cocktail_id:int):
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'), 
                           port=int(os.getenv('MYSQL_PORT')), 
                           user=os.getenv('MYSQL_USER'),
                           password=os.getenv('MYSQL_PASSWORD'), 
                           db=os.getenv('MYSQL_DATABASE'), charset='utf8')
    cur = conn.cursor()
    sql= """DELETE from donelist_cocktail WHERE user_id=%s AND cocktail_id=%s"""
    try:
        cur.execute(sql,(user_id, cocktail_id))
        conn.commit()
        return {"message":"술 donelist 삭제 성공"},200
    except: 
        abort(500, "술 donelist 삭제 실패")

# 칵테일 레시피 모아보기
def my_cocktail_recipe(user_id:int):
    cocktails = Cocktail.query.filter_by(author_id=user_id).all()

    return cocktails,200

# 내가쓴 리뷰 모아보기
def my_review(user_id:int):
    reviews = Review.query.filter_by(user_id = user_id).all()
    
    return reviews,200
