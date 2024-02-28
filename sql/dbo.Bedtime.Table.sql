USE [BedtimeTracker];
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Bedtime](
	[BedtimeDate] [date] NOT NULL,
	[Success] [bit] NOT NULL,
	
	CONSTRAINT [PK_Bedtime] PRIMARY KEY CLUSTERED ([BedtimeDate] ASC) 
);