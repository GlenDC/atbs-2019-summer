import random

contact_info_rows = """John Manning	679 Michelle Ridge, Douglasshire, NM 28291	rbrown@hotmail.com
Christopher Levine	595 Cowan Bridge, Caldwellville, MA 62210	brittany25@fisher.biz
Jose Marshall	142 Catherine Meadow Suite 873, Johnsonmouth, TN 48808	dana00@gmail.com
Keith Hunt	4785 Marshall Park Apt. 751, South Jameshaven, ID 43300	jillian44@hendricks-koch.net
Pamela Morton	5689 Andrew Square Suite 927, East Calvinmouth, TN 96537	daniel88@hotmail.com
Randall Carter	0372 Kevin River Apt. 584, Lake Saraburgh, IL 21501	johnsonjerry@carlson.com
Kimberly Mcdaniel	685 Dwayne Inlet, Holtstad, MT 47432	jacqueline46@sanford-johnson.com
Tammy Harrison	59722 Jenkins Center Apt. 652, Paceview, IA 65945	dphillips@hammond.com
Katherine Norman	51703 Donna Islands Apt. 482, Teresaton, MD 88147	rlewis@weber-franklin.com
Richard Shea	9702 Bush Mills, Charlesfort, GA 92670	stephanie93@hotmail.com
Amanda King	681 Hinton Ports Apt. 068, Nicholaston, WA 63920	lancecollins@hotmail.com
Cynthia Barry	95912 Walker Centers Suite 848, New Luisborough, WV 20557	taylorprice@yahoo.com
Christopher Weber	67076 Adam Ford, South Vanessa, ME 03183	eobrien@hotmail.com
Elaine Montgomery	5089 Levy Common, West Carolview, HI 59290	cwilson@hotmail.com
Gene Lopez	22347 Jones Crossing Apt. 052, Johnland, FL 30228	steven82@cordova-williams.com
Eric Richard	690 Aaron Summit Apt. 357, Craigburgh, UT 49049	sandrataylor@yahoo.com
Rebecca Raymond	0929 Clark Via, Ericachester, DC 71869	nguyenbrittany@hotmail.com
Brian Russell	8055 Michael Via, Port Angela, DC 42709	david69@garcia.info
Benjamin Hall	18267 Justin Springs, Villahaven, NE 90802	virginiastone@allen-zhang.biz
Jason Cook	1123 Gomez Lakes, New Sally, WI 96205	psimmons@gmail.com
Patrick Cox	9729 Savannah Cove Apt. 721, West Saraside, RI 08409	moorewilliam@brooks.biz
Tanner Sullivan	23509 Molly Port Apt. 346, Lake Ryanland, MN 87681	carolmoore@pugh.com
Amber Herrera	3507 Simpson Points Suite 924, Jesseview, MI 30184	sanderstimothy@hotmail.com
Travis Carter	30375 Andre Plains Suite 875, Millerville, SD 40575	fsmith@baldwin.info
Jessica Wilson	6207 Jones Green Apt. 431, Port Scott, MO 47336	jacoblucas@gmail.com
Cheryl Bennett	800 Gill Light, Lake Craig, MO 90246	emmawhite@campbell-nunez.com
Linda Schneider	13521 James Lodge Suite 174, Davisfurt, NY 57185	ychavez@lee.org
Alyssa Lynch	939 Billy Rapids, West Michelle, AL 80525	richardsbrian@hotmail.com
Tina Mendoza	4264 Robert Spring, Rodriguezhaven, IN 94192	angela12@alexander.biz
Danielle Stark	84708 Watson Club, Jimenezfurt, TN 88377	nrose@le.com
Stephen Wright	PSC 8889, Box 3954, APO AP 97801	martinpaula@hotmail.com
Sabrina Murphy	7952 Victoria Ville, Connorstad, VA 97089	erik81@richards.net
Jerome White	02570 Linda Ports Suite 461, North Michaelview, RI 12714	cantrellcolleen@burnett-luna.net
David Ramirez	2398 Clark Mall, Davisfurt, MN 76072	christopher45@richardson.org
Edwin Adams	2109 Klein Meadow Apt. 668, East Kellie, NC 75913	amberknight@moore.com
Joseph Wilson	015 Tracy Valleys Apt. 021, West Williamton, TX 20914	brandon58@greene-garcia.org
Brent Archer	906 Bell Forge, East Kenneth, WI 02161	parkerbrandon@yahoo.com
Troy Rios	04855 Christina Cove Apt. 800, Dianaville, CT 82775	bnelson@gmail.com
Robert Robinson	9479 Sarah Points Suite 114, Pricefort, NM 51124	johnsonstacy@yahoo.com
Edward Young Jr.	643 Jessica Shores Apt. 526, Teresaport, OK 85258	lisafoley@jensen.org
Timothy Carson	534 Dan Union, Walterbury, IN 81919	john67@hotmail.com
Fernando Greene	801 Powell Fork, East Randy, AK 99682	jschwartz@hudson.com
Ryan Gonzalez	882 Diane Plains, Port Daniel, AZ 57381	alexandersmith@mitchell.biz
David White	612 Holly Dam, Thorntonville, NY 64355	watsonshannon@gmail.com
Patrick Stewart	9906 Lindsay Plaza, Garnertown, NM 96098	rubiosharon@zuniga-montgomery.info
Gregory West	936 Williams Neck, Howeborough, MD 21974	kleinsandra@hotmail.com
Robert Bowers	401 Martin Brook Apt. 411, Rodriguezbury, ME 31985	gregorybuchanan@kramer-cross.com
Trevor Bruce	15334 Mendoza Mews Suite 892, West Garymouth, SD 35454	williamlucas@adams.com
Dennis Ramirez	45723 Bennett Village Suite 979, South Cynthia, KY 33527	schmittjohn@frank-francis.org
Danielle Bolton	58132 Ward Village Apt. 921, Millerview, LA 16144	meyerjessica@garcia.com
Tasha Sanchez	317 Williams Lane, South Daniel, LA 80145	blindsey@hotmail.com
Zachary Thomas	914 Nicholas Hollow, Lake Hannah, NH 97591	melissalloyd@yahoo.com
Mary Hill MD	12599 Hanna Passage Suite 451, Lawrenceside, SD 26097	uyoung@nguyen-patterson.com
Kelly Lee	423 Glenn Plaza, Lake Lisa, PA 76134	michellemcgee@gmail.com
Joseph Freeman	PSC 4416, Box 8756, APO AE 98462	rosecarrie@gmail.com
Mitchell Ward	6471 Melissa Village Suite 891, Lake Gregorystad, WA 83519	micheleharrison@walker.com
Cathy Campbell	603 Esparza Inlet, Harrellton, NM 21563	bfrazier@jimenez.com
Sheri Washington	9284 Tony Drive, East Erika, KY 61302	lewisryan@hotmail.com
Jasmine Anderson	38033 Holly Vista Apt. 714, Leemouth, IN 47942	mooredonna@hotmail.com
Corey Bailey	2149 Lloyd Crescent Apt. 034, New Brian, GA 02020	cjarvis@gmail.com
Kayla Rogers	USNV Stein, FPO AP 05140	ericaharris@gmail.com
Jennifer Taylor	07101 Walsh Crossroad, Raymondshire, UT 09296	mccoyjamie@yahoo.com
Shannon Cooper	0063 Sanchez Mount, Edwardston, VA 53232	sroth@gmail.com
Ian Shepherd	37633 Roberson Village, New Elizabethfurt, WI 34064	trobinson@turner.com
Sean Hoffman	428 Fisher Locks, Lake Henry, IL 14723	cervanteskatherine@charles.com
James Davis	825 Lopez Fields Suite 255, Evanschester, WV 01236	qsmith@gmail.com
Heather Bush	6927 Jonathan Mount Suite 749, South Rogertown, MN 69763	eoneal@williams.com
John Carter	438 Murphy Green, Patrickmouth, VA 73496	beth51@gmail.com
Dr. Debra Rodriguez	229 Mckenzie Field, West Jon, IN 26910	ssullivan@hotmail.com
Harold Smith	964 Jonathan Wells, Kimbury, CO 37230	michael58@kent.com
Jamie Frazier	660 Ashley Hollow, New Shawn, CA 57442	jamescunningham@yahoo.com
Kathy Crawford	70383 Moore Branch, South Christopher, OR 46810	stephanieleon@dominguez.com
Amber Wright	2387 Christine Mall, Greenbury, KS 76699	xnunez@yahoo.com
Michael Duncan	80164 Rush Villages, Hendrixland, MS 87626	campbelljose@james.com
Daniel Duran	64756 Kaitlin Street, Hendricksshire, CO 61604	jennifer79@yahoo.com
Nathan Gray	4264 Marquez Lights, Port Barrymouth, HI 25670	nicholasmitchell@hotmail.com
Carl Brennan	87596 Jensen Courts, Heidistad, CT 22391	smithconnie@hotmail.com
Roger Hunt	49838 Marvin Hill, New Amybury, MS 12797	xmendoza@hotmail.com
Julia Crosby	483 Brown Circles Suite 280, Pittmanmouth, IN 92259	connie38@yahoo.com
Robert Villegas	9965 Gonzalez Locks, Theresatown, ID 83615	tlynn@salazar-nelson.info
Courtney Gordon	965 Thomas Inlet Apt. 714, West Dylanhaven, OH 76092	jessicamorris@weaver-valencia.com
Erica Wells	1779 Hudson Squares Apt. 678, West Jonathanfurt, OR 81414	anthonycraig@yahoo.com
Christopher Rose	0625 Terri Cliffs Apt. 329, North Eric, WI 09483	patricia94@hanson-knight.com
Tracy Carey	0334 Knox Court Apt. 902, Port Thomas, OK 53619	joseph18@hammond-trevino.net
Matthew Moon	21972 Williams Street Suite 560, East Matthewmouth, NC 13302	susan25@yahoo.com
Melissa Miller	874 Trevino Shore Suite 682, Port Jason, IA 48883	wumathew@reid.org
James Townsend	32046 Sarah Path, Port Tamara, OK 63530	pwalker@hotmail.com
Joseph Torres	7338 Marquez Falls, Matthewton, NC 86690	sanchezchristopher@gmail.com
Bryce Small	665 Thomas Rapids Suite 574, Lake Kimberly, ME 71044	blackburndanielle@robles.com
Julie Brown	7716 Krista Isle, Roberthaven, DE 54567	rachel02@gmail.com
Amanda Martinez	26706 Johnson Groves Apt. 818, Port Katelynport, KY 64259	dennis86@gmail.com
Mark Wright	525 Alan Grove Apt. 920, Carsonview, SC 26664	bartonkatherine@lewis-olson.info
Haley Giles	018 Schmidt Meadows Apt. 138, West Kellifurt, MN 31557	diana88@yahoo.com
Kelly Shepherd	2927 Molly Point, Bryantstad, CA 30489	ashley32@hotmail.com
Anthony Patel	3954 Roberts Crossing, New Jackiemouth, CT 48918	thorn@lindsey.org
Melanie Castro	868 Kelly Flat Apt. 419, Elliottbury, MN 74122	garciastephanie@yahoo.com
Angela Howard	271 Young Park, North Jason, NY 82507	grimesmichelle@hall.com
Brittany Robinson	736 Kane Fort Apt. 293, Johnhaven, GA 99750	gwalters@hotmail.com
Jennifer Brooks	617 Johnson Lane, Lake Robertport, CA 72527	sextonsamantha@campbell.com
""".splitlines()

wallet_info_rows = """David Ramirez	01d26e218457159588b1ed984ea7c896ba31bdda542f2840fe29025a3115a311949642fe74c55b
Jennifer Brooks	0118bb893688b995c293d3c7bbae9bab7f8b715f7e0cb4444157a2cbf3e074f7bb622181f3b0d9
Gene Lopez	01739999812892cfb237c2c2f802b2950172ef52244919b86440e374d2688a1001db4d352977e8
Benjamin Hall	0160200f9bf462cdef1fca9191bed96d505fa475a296688d235255cdbb9c646197d35f966e5b34
Joseph Torres	01fc9ab8ec5b4ac4765d4536d982f421043c6a3f6e9bfcc10428ce779fa01472c1c835df038660
Joseph Wilson	01968eeadbd1ae34b7cf47d02dad89825929a7212b908665eae966017838edbb3871ce992fa158
Harold Smith	01ba82d5e7cac26c85139e4ccc4bde8b8e2fd9c9af08c193ce879675404462247aba2f1822e9d3
Fernando Greene	010601d4cccd5049885614c87f37721279c7cb258f4630ce4c95d5227b89e761b5bbec3b7e7263
Sean Hoffman	01d3f44c57a6be9254422df58610041c6397645c55b0354283c8e2e13bd649f7ebe19857afe217
Brittany Robinson	01f08344e622253df3140eb8e4b869f02c7e67c83c184083300fb4f2d0affc36eb76f102d2527f
Christopher Rose	015592caa4964a90e3de03df8390889301efb212a393cb77d24c87e699d460db026dad89be2e0a
Danielle Bolton	01897b410acf3438d0dcb62feb8b56db52d4b2a1b86cbc243c48d05b5b41e01125dd9ba3ef5de4
Katherine Norman	0134b452bbaa639975a2ac4c88561abc72b3873462e39610af256d9c5975389ea4d9c66d276806
Gregory West	01c82dbabb83ad2ff00af1ef666d8013f469542b05647293c16b408c0aaa098577ac3a3be17408
Shannon Cooper	01a0f37d1dbf4f73448e1b2640b8fd313e77b0892f2631ec613fefaf79ae15605b15ad2780d02c
Tanner Sullivan	0110cee865324701fac2a53946ab4dac3e226cde55cad86fa21816154f138e18d7ee6abb755a55
Troy Rios	01d9e18f74010096ff7b94b1db4b60382be2a59963e4644db59f25e6ccf63d2380012b3d0622aa
Elaine Montgomery	01b6ef19aee9126df7804a3a7c20d93de7f82ca3c3aa5986aa14f0a859fc86b552a434ab7a3edc
Amber Herrera	0163d34a0c599efe2e6ad607b34233bd69368af7522c3f6d0aba6fda3a1a82d3fbcfc09712b2ab
Dennis Ramirez	01316e230864ae7555e9e057aa33b4dfcbb82ba1e74922b5bca92b2cdebe5d2cf02ca675dbcfdf
Eric Richard	0191d3cdf9179f30c7dda5fb85460e952587ac6402e74f26dbc8dff8f07f2be1408f51786f89ad
Heather Bush	01ae56651e6db2da0c2258c86fbda9f4aeb2fe854f99b90e84645fed728567b4b43c95fac53a94
Linda Schneider	017f33b7f8f85e21f7304eb2b9636844b7d062ebf90af2fbc8c49bcceb9a2984b9e84f6e75f051
Patrick Cox	0118ec40e127f175cd5deb34f86ad06625dc92ae88829d8d9cf40575d942fca19dcc1d2c522583
Nathan Gray	01b4d8b6dd2f695664155793797b2ed5a22df6ac8bc9ff1ca7bdcfa950a77db6ab5c4cb934da90
Sheri Washington	01750e532fcef9a35e760d5a1b7888463ff431c483ffb18c077dde0a4004213d455ab96cbc29dc
Randall Carter	012728be1c0a4f14cedfdd7538d1635211bedb3b4c4047ff9e62f94a608db6a964d9c501dd56a8
Cathy Campbell	018e773de71cbe93b1f9d76e14bf24a99e474df106e55e6aea5af603fd7b907c7c350a4275d48a
Zachary Thomas	01fc1e47097e1fe958efb86c80a9eac9f80302c94564aa7653c7dc2cc4f9a676f8210b0a5a3834
Jennifer Taylor	01464c9c4929e367f0f481fbaeb7b37c20ff89039568e998fd822f8c2277c0da545c71effe5758
Richard Shea	0128ed4e5883ff0086bda950244eaa2cd9a156a7007769b0aef40f3bba1d3db0b2abdbeebb8605
Brent Archer	010fb3f77002ffa4ac49133d968abc99c7cf50629711c34a04e05c32379adb902518c72f0b9570
Kimberly Mcdaniel	0116d916540bd5d4a2222918471d6c76523542e6102ca8cc2ab40dce5e5db221cd80e22d46a00a
Robert Robinson	01550f0f680bcdd40eda433f383e11cfafabcf8edc95d0bb1e48b5db4be0b65920a28bd27dcf37
Jose Marshall	01a0fe2be174d878eed76e585eafee86d883409abc51fd9d39a28ba751f076ae20c75ed238da3c
Rebecca Raymond	0191db51d0268f00f14ff3f102d4145c69ca7d8ab7821decf333073484b1bdd253df5a3681b421
Bryce Small	01e6facae96ba2fe89bb6a95c51e41b2ff575b67aa5a7d598953b522609bbcbde4cf0fe1c41780
Tina Mendoza	01967791380becc0c803ea0f969e1576a8bb050bd88bc434b4ec3c570dfb45f6608c7923a99eb9
Jasmine Anderson	017908a5e9b165c11d062347d4c9d7faa795d31a0d68d9125193ce4c6ea8573c1404354910271d
Kelly Lee	01e1cf6087663527c66e9c15fdd318712fcd766d073fbd3446bda99367679bb9ac4b61c44ecd33
Joseph Freeman	011607aef42d0e2aad49ef76072cd0ddc89d5b6f6180509051d61e752fa4d1d3d0a3f05788c88d
Melanie Castro	013c52ae78bbf63771b884b0918e2fdadc0e661b94c821be8ce327d21adad2dd7a7cb3870f1a33
Tammy Harrison	01b2f6af019ea1a1ad42c407d117b70499d48e5e45d94f29e526e37ff7f3a4479234b2e8e1cca5
Mark Wright	017a08a3ee538453d3a02ddff2772fa83b16edb30d19ddeb30f4ad4f07189cdfe08a9affe16948
Amanda King	01ec1f204b58733877b6c89927ab4f83eb8fb5d26718ee7b9e8831fca15603535acc09d559958e
Julia Crosby	010498ba98bdb5306d7ab1eee5607e0856928e8b6a179d7511d3eeb1946e94cbef62f4cdddc16c
Kayla Rogers	017a7b5ece3ad8a075a7423600fe10a5866a054f216a274a6a1f758a26935a3979ac5a58f91f89
Dr. Debra Rodriguez	0128bda5170deec1255f74143f3d3107f89db96f977130947f89d0c670008ba7f9c496fe17d3d8
Matthew Moon	01be276cf872adf8aa7403a43dfd4314c9dac6443167d4bdaf32facb931d588011fcc555886b92
Mary Hill MD	01f4a3e41b0bd3691200a5b3018950006f91fc1b04076e7ea5e5d874a84aa5b1452321beddafcc
Danielle Stark	01050717a2d1f2ae41c692864034365834c940b1ecde03f41fc91c59570425a500613334a069fa
Anthony Patel	01fcac24f19d17230c824b4d7b891c4b8835300c9d8e5f3688883d613f0a9f50cc9b3ce2b9f511
Carl Brennan	01069904669fe5190591f8548e35ed5a12e17e636b4398e75d54671ec3b38cface9628db255fca
Kelly Shepherd	01eb7c9f2b236438915f633afa368768bfd12d1cb6106b731518941a7e9da113ade1456b6608b2
Cynthia Barry	012f2033ace1b0b17af28c02cc6e38d9e510d0db6c37d06ad036fdf611f32a4e3209960cee3993
""".splitlines()

data = {}
for row in contact_info_rows:
    columns = row.split("\t")
    data[columns[0]] = {
        "address": columns[1],
        "email": columns[2],
    }
for row in wallet_info_rows:
    columns = row.split("\t")
    data[columns[0]]["wallet"] = columns[1]

winner_count = 0
while winner_count < 10:
    candidates = len(data)
    name = random.choice(list(data.keys()))
    user = data[name]
    if "wallet" in user:
        print("send an email to {} at {} and send prize to {}".format(name, user["email"], user["wallet"]))
        del data[name]
        winner_count += 1
