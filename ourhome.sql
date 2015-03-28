
### TRANSACTIONS IN ADMIN_QUERIES.JAVA ###

"CREATE VIEW avg_transactions AS "
			"SELECT time, avg(price) as avg_t "
			"FROM Transaction " 
			"GROUP BY time";

"SELECT AT.time as time, MIN(AT.avg_t) "
				"FROM avg_transactions AT";
"SELECT AT.time as time,  MAX(AT.avg_t) "
				"FROM avg_transactions AT";

"CREATE VIEW daily_transactions AS "
			" SELECT T.time, SUM(price) as sum "
			"FROM Transaction T " 
			"GROUP BY T.time ";

"select AVG(DT.sum) as avg"
				"from daily_transactions DT";

"SELECT sum(T.price) as total, T.time 
FROM Transaction T, ListingPostedIsIn LP, Location L 
where LP.listingId = T.listingId AND L.postalCode = LP.postalCode 
group by time";

"UPDATE ListingPostedIsIn "
			"SET rating = ?"
			"WHERE listingId = ?";


"SELECT T.transactionId, T.price, T.time, L.city, LP.address FROM Transaction T, ListingPostedIsIn LP, Location L "
			"where LP.listingId = T.listingId AND L.postalCode = LP.postalCode AND T.time = TRUNC(SYSDATE)";

"SELECT T.transactionId, T.price, T.time, L.city, LP.address 
FROM Transaction T, ListingPostedIsIn LP, Location L 
where LP.listingId = T.listingId AND L.postalCode = LP.postalCode";

"SELECT * 
FROM ListingPostedIsIn LP, Location L 
WHERE L.postalCode = LP.postalCode";


"SELECT h.governmentId FROM Host h WHERE h.email = ?";

"SELECT * FROM RegisteredUser";

"INSERT INTO Verifies VALUES (?, ?)"

"Select R.email "
			"FROM RegisteredUser R "
			"MINUS "
			"(Select distinct H.email "
			"FROM ListingPostedIsIn L, Host H "
			"WHERE l.governmentId = H.governmentId UNION "
			"Select t.email from TransactionIdAndEmail t)"

"SELECT DISTINCT * FROM admin WHERE adminId = "  + adminId + " AND password LIKE '%" + password + "%'";

"SELECT * FROM RegisteredUser R WHERE R.name = ?"

"SELECT R.name, R.email " 
			"FROM Host H, Verifies V, RegisteredUser R "
			"WHERE H.governmentId = V.governmentId AND H.email = R.email";

####################################################################################


#### TRANSACTIONS IN USER_QUERIES.JAVA ####

"UPDATE AmenitiesIncluded  "
				"SET tv  = ?, kitchen = ?, internet = ?, laundry = ?, toiletries = ?"
				"WHERE listingId = ?"

"UPDATE ListingPostedIsIn "
			"SET price = ?, capacity = ?, private = ?"
			"WHERE listingId = ?"

"INSERT INTO Location (postalCode, city, country) "
					"VALUES (? ,?, ?)"

"Select postalCode from Location"

"delete FROM Transaction WHERE transactionId = ?"
"delete FROM TransactionIdAndEmail WHERE transactionId = ?"
"delete FROM MakesReservation WHERE listingId = ?"
"delete FROM ListingPostedIsIn WHERE listingId = ?"
"select * FROM MakesReservation WHERE listingId = ?"


"SELECT h.governmentId FROM Host h WHERE h.email = ?"

"INSERT INTO AmenitiesIncluded (amenitiesId, listingId, tv, kitchen, internet, laundry, toiletries) "
				"values (amenities_seq.nextval, ?, ?, ?, ?, ?, ?)"

"Select listingId from ListingPostedIsIn"

"INSERT INTO ListingPostedIsIn (listingId, price, capacity, private, rating, governmentId, postalCode, address) "
			"VALUES (listing_seq.nextval, ?, ?, ?, ?, ? ,?, ?)"

"SELECT * FROM RegisteredUser r, ListingPostedIsIn l, Host h "
			"WHERE r.email = ? and r.email = h.email and l.governmentId = h.governmentId"

"select *"
	"from transaction t, makesreservation mr, transactionidandemail te "
	"where t.transactionid = te.transactionId and "
	"t.transactionid = mr.transactionid and "
	"te.email like ? "
	"order by t.time"

"SELECT r. email, sum(t.price) as total "
			"FROM RegisteredUser R, Transaction T, TransactionIdAndEmail TE "
			"WHERE R.email = TE.email AND T.transactionId = TE.transactionId "
			"GROUP BY r.email"

##########################################################################################


#### TRANSACTIONS IN LISTING.JAVA ####

"SELECT loc.city, loc.country, AVG(list.rating), AVG(list.price) as avp "
			"from Location loc, ListingPostedIsIn list "
			"where list.postalCode = loc.postalCode "
			"group by loc.city, loc.country"

"CREATE VIEW min_price AS " +
				"SELECT L.city, LP.postalCode, MIN(LP.price) as min " +
				"FROM ListingPostedIsIn LP, Location L " +
				"WHERE LP.postalCode = L.postalCode AND LP.rating >= ALL " +
					"(select AVG(LP2.rating) as avgRating " +
					"from ListingPostedIsIn LP2, Location L2 " +
					"where LP2.postalCode = L2.postalCode AND L2.city = L.city " +
					"group by L2.city, LP2.postalCode) " +
					"GROUP by L.city, LP.postalCode"
"select M.city, L.country, MIN(M.min) as min " +
							 "from min_price M, ListingPostedIsIn LP, Location L " +
							 "where LP.postalCode = M.postalCode AND L.postalCode = LP.postalCode " +
							 "GROUP BY M.city, L.country " +
							 "ORDER BY min ASC"


"INSERT INTO ListingIsPostedIn VALUES (?, ?, ?, "
				"?, NULL, ?, ? ,?)"

"DELETE FROM ListingIsPostedIn WHERE listingId = ?"


"SELECT DISTINCT * FROM ListingPostedIsIn l, AmenitiesIncluded a, Host h, RegisteredUser r WHERE "
				"h.governmentId = l.governmentId AND "
				"a.listingId = l.listingId AND "
				"r.email = h.email AND "
				"l.capacity >= " + capacity
				"  AND a.tv like '%" +  amenities[0] + "%' and a.laundry like '%" + amenities[1] + "%' and a.toiletries like '%" + amenities[2] + "%' and a.kitchen like '%" + amenities[3] +"%' AND"
				" l.listingId in"
				"(SELECT DISTINCT l.listingId FROM Location loc "
				"WHERE l.postalCode = loc.postalCode AND loc.city like '%" + city + "%') "
				"AND l.listingId not in"
				"(SELECT DISTINCT l.listingId FROM MakesReservation m WHERE l.listingId = m.listingId "
				"AND (m.checkindate <= TO_DATE('" + cdIn + "', 'YYYY-MM-DD') AND"
				" m.checkoutdate >= TO_DATE('" +  cdOut + "','YYYY-MM-DD'))) " 
				"ORDER BY " + sortBy
"(SELECT AVG(LP.rating) " 
				"FROM ListingPostedIsIn LP, Location L "
				"WHERE LP.postalCode = L.postalCode "
				"GROUP BY (LP.city, LP.postalCode)) "



"CREATE VIEW min_price AS "
				"SELECT L.city, LP.postalCode, MIN(LP.price) as min "
				"FROM ListingPostedIsIn LP, Location L"
				"WHERE LP.postalCode = L.postalCode AND"
				"LP.rating >= "
				nestedAvg
				"GROUP BY (LP.city, LP.postalCode)"


"SELECT LP.address, M.city, M.postalCode, M.min "
				"FROM min_price M, ListingPostedIsIn LP "
				"WHERE LP.postalCode = M.postalCode "

####################################################################################


#### TRANSACTIONS IN USER_REGISTER.JAVA ########

"SELECT email FROM RegisteredUser WHERE email like '%" + userEmail + "%'"

"INSERT INTO RegisteredUser VALUES ('"  + userEmail + "', '" + userName +  "', '" + userPassword + "')"

####################################################################################

#### TRANSACTION IN INDEX.JAVA ######

"select * from ListingPostedIsIn l, Host h, RegisteredUser r where h.governmentId = l.governmentId and r.email = h.email and l.listingId in " +
						"(select distinct l.listingId from Location loc where l.postalCode = loc.postalCode and loc.city like '%" + city + "%')"

"SELECT * FROM RegisteredUser WHERE email LIKE '%"  + userId + "%' AND password LIKE '%" + userPassword + "%'"

"DROP VIEW min_price CASCADE CONSTRAINTS" # We have a residual view from the transaction in listing.java. Due to a bug we removed it here.

####################################################################################

#### TRANSACTIONS IN USERLOGIN.JAVA #####

"SELECT * FROM RegisteredUser WHERE email LIKE '%"  + userEmail + "%' AND password LIKE '%" + userPassword.toString() + "%'"

####################################################################################


#### TRANSACTIONS IN MAKERESERVATION.JAVA #####

"select distinct * from ListingPostedIsIn l, Host h, RegisteredUser r, Location loc where l.governmentId = h.governmentId "
			"and l.postalCode = loc.postalCode and h.email = r.email and l.listingId = " + list.getSelectedId()

####################################################################################


#### TRANSACTIONS IN RESERVATION.JAVA #####

"INSERT INTO Transaction (transactionId, price, time, listingId) VALUES (trans_seq.nextval, ?, ?, ?)"

"SELECT MAX(transactionId) as transactionId FROM Transaction"

"INSERT INTO MakesReservation (reservationId, listingId, "
			"checkindate, checkoutdate, numberOfGuests, transactionId) "
			"VALUES (resv_seq.nextval, ?,?,?,?,?)"

"DELETE FROM MakesReservation WHERE listingId = ? AND transactionId = ? "
			"AND checkindate LIKE ? AND checkoutdate LIKE ?"

"INSERT INTO TransactionIdAndEmail (transactionId, email) VALUES (?,?)"

"INSERT INTO PayPalTransaction (transactionId, email) VALUES (?, ?)"

"INSERT INTO CreditCardInfo (cardNumber, company, cardHolderName, expirationDate) "
			"VALUES (?, ?, ?, ?)"

"INSERT INTO CreditCardTransaction(transactionId, cardNumber) VALUES (?,?) "


####################################################################################






