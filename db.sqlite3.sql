

CREATE TABLE "radio_studioradio" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"messageCourant_text"	varchar(255) NOT NULL
);

CREATE TABLE"radio_posteradio" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"messageCourant_text"	varchar(255) NOT NULL,
	"StudioRadio_id_id"	bigint NOT NULL,
	FOREIGN KEY("StudioRadio_id_id") REFERENCES "radio_studioradio"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE  "radio_resistant" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pseudo"	varchar(45) NOT NULL,
	"studioRadio_id"	bigint NOT NULL,
	FOREIGN KEY("studioRadio_id") REFERENCES "radio_studioradio"("id") DEFERRABLE INITIALLY DEFERRED
);


CREATE TABLE "radio_message" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"message_text"	varchar(255) NOT NULL,
	"pub_date"	datetime
);


CREATE TABLE "radio_action" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_text"	varchar(45) NOT NULL,
	"message_id_id"	bigint NOT NULL UNIQUE,
	FOREIGN KEY("message_id_id") REFERENCES "radio_message"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "radio_resistant_has_message" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"message_id_id"	bigint NOT NULL,
	"resistant_id_id"	bigint NOT NULL,
	FOREIGN KEY("resistant_id_id") REFERENCES "radio_resistant"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("message_id_id") REFERENCES "radio_message"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "radio_envahisseur" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pseudo"	varchar(45) NOT NULL,
	"PosteRadio_id_id"	bigint NOT NULL UNIQUE,
	FOREIGN KEY("PosteRadio_id_id") REFERENCES "radio_posteradio"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "radio_groupeclandestin" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pseudo"	varchar(45) NOT NULL,
	"messageAttendu_text"	varchar(255) NOT NULL,
	"PosteRadio_id_id"	bigint NOT NULL UNIQUE,
	FOREIGN KEY("PosteRadio_id_id") REFERENCES "radio_posteradio"("id") DEFERRABLE INITIALLY DEFERRED
);






