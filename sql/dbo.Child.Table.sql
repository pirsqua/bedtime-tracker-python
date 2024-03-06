USE [BedtimeTracker];
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Child](
	[ChildId] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](100) NOT NULL,
	
	CONSTRAINT [PK_Child] PRIMARY KEY CLUSTERED ([ChildId] ASC)
);