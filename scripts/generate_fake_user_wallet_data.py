import os, random

names = """
John Manning
Christopher Levine
Jose Marshall
Keith Hunt
Pamela Morton
Randall Carter
Kimberly Mcdaniel
Tammy Harrison
Katherine Norman
Richard Shea
Amanda King
Cynthia Barry
Christopher Weber
Elaine Montgomery
Gene Lopez
Eric Richard
Rebecca Raymond
Brian Russell
Benjamin Hall
Jason Cook
Patrick Cox
Tanner Sullivan
Amber Herrera
Travis Carter
Jessica Wilson
Cheryl Bennett
Linda Schneider
Alyssa Lynch
Tina Mendoza
Danielle Stark
Stephen Wright
Sabrina Murphy
Jerome White
David Ramirez
Edwin Adams
Joseph Wilson
Brent Archer
Troy Rios
Robert Robinson
Edward Young Jr.
Timothy Carson
Fernando Greene
Ryan Gonzalez
David White
Patrick Stewart
Gregory West
Robert Bowers
Trevor Bruce
Dennis Ramirez
Danielle Bolton
Tasha Sanchez
Zachary Thomas
Mary Hill MD
Kelly Lee
Joseph Freeman
Mitchell Ward
Cathy Campbell
Sheri Washington
Jasmine Anderson
Corey Bailey
Kayla Rogers
Jennifer Taylor
Shannon Cooper
Ian Shepherd
Sean Hoffman
James Davis
Heather Bush
John Carter
Dr. Debra Rodriguez
Harold Smith
Jamie Frazier
Kathy Crawford
Amber Wright
Michael Duncan
Daniel Duran
Nathan Gray
Carl Brennan
Roger Hunt
Julia Crosby
Robert Villegas
Courtney Gordon
Erica Wells
Christopher Rose
Tracy Carey
Matthew Moon
Melissa Miller
James Townsend
Joseph Torres
Bryce Small
Julie Brown
Amanda Martinez
Mark Wright
Haley Giles
Kelly Shepherd
Anthony Patel
Melanie Castro
Angela Howard
Brittany Robinson
Jennifer Brooks
""".splitlines()[1:]
random.shuffle(names)

print("name,wallet")
for name in names:
    if bool(random.getrandbits(1)):
        print("\"{}\",\"01{}\"".format(name, os.urandom(38).hex()))
