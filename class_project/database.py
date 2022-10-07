#!/usr/bin/env python3
"""The database for the inventory system"""
# import
import sqlite3


def connect():
    """establish connection to the database"""
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, name text"
                ", qty real, price real, date text)")
    conn.commit()
    conn.close()


def insert(name, price, qty, date):
    """insert data to the database"""
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO item VALUES (NULL,?,?,?,?)", (name, price, qty, date))
    conn.commit()
    conn.close()


def view():
    """grab all inventory from the database"""
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM item")
    views = cur.fetchall()
    conn.close()
    return views


def search(name="", price="", qty="", date=""):
    """grab provided user input"""
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM item WHERE name=? OR price=? OR qty=? OR date=?",
                (name, price, qty, date))
    searches = cur.fetchall()
    conn.close()
    return searches


def delete(item_id):
    """delete the selected item"""
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM item WHERE id=?", (item_id,))
    conn.commit()
    conn.close()


def update(item_id, name, price, qty, date):
    """update the list"""
    conn = sqlite3.connect("item.db")
    cur = conn.cursor()
    cur.execute("UPDATE item SET name=?,price=?, qty=?, date=? WHERE id=?",
                (name, price, qty, date, item_id))
    conn.commit()
    conn.close()


# connect as soon as main starts
connect()
