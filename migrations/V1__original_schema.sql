--
-- PostgreSQL database dump
--

-- Dumped from database version 10.0
-- Dumped by pg_dump version 10.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: api_ip_whitelist; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE api_ip_whitelist (
    id integer NOT NULL,
    dt_created timestamp(0) without time zone DEFAULT now() NOT NULL,
    ip_address inet NOT NULL,
    comment character varying(255)
);


--
-- Name: api_ip_whitelist_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE api_ip_whitelist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: api_ip_whitelist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE api_ip_whitelist_id_seq OWNED BY api_ip_whitelist.id;


--
-- Name: cli; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE cli (
    id integer NOT NULL,
    dt_created timestamp(0) without time zone DEFAULT now() NOT NULL,
    name character varying(255) NOT NULL,
    pid integer,
    dt_start timestamp(0) without time zone,
    dt_finish timestamp(0) without time zone
);


--
-- Name: cli_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE cli_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cli_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE cli_id_seq OWNED BY cli.id;


--
-- Name: api_ip_whitelist id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY api_ip_whitelist ALTER COLUMN id SET DEFAULT nextval('api_ip_whitelist_id_seq'::regclass);


--
-- Name: cli id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY cli ALTER COLUMN id SET DEFAULT nextval('cli_id_seq'::regclass);


--
-- Name: api_ip_whitelist api_ip_whitelist_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY api_ip_whitelist
    ADD CONSTRAINT api_ip_whitelist_pkey PRIMARY KEY (id);


--
-- Name: cli crons_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY cli
    ADD CONSTRAINT crons_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

