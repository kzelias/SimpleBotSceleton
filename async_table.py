from create_bot import bot


async def table_add(data: tuple) -> None:
    cur = await bot.db_con.cursor()
    from_user, button_name, time = data
    query = """
                INSERT INTO 
                    clicks 
                    (user_id, username, button_name, time, first_name, last_name, is_bot, 
                    language_code, is_premium, added_to_attachment_menu, 
                    can_join_groups, can_read_all_group_messages, supports_inline_queries)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
    await cur.execute(
        query,
        (
            from_user.id,
            from_user.username,
            button_name,
            time,
            from_user.first_name,
            from_user.last_name,
            int(from_user.is_bot) if from_user.is_bot else None,
            from_user.language_code,
            int(from_user.is_premium) if from_user.is_premium else None,
            int(from_user.added_to_attachment_menu)
            if from_user.added_to_attachment_menu
            else None,
            int(from_user.can_join_groups) if from_user.can_join_groups else None,
            int(from_user.can_read_all_group_messages)
            if from_user.can_read_all_group_messages
            else None,
            int(from_user.supports_inline_queries)
            if from_user.supports_inline_queries
            else None,
        ),
    )
    await bot.db_con.commit()


async def table_add_follower(data: tuple) -> None:
    cur = await bot.db_con.cursor()
    from_user, button_name, time = data
    query = """
                INSERT INTO 
                    followers 
                    (user_id, username, button_name, time, first_name, last_name, is_bot, 
                    language_code, is_premium, added_to_attachment_menu, 
                    can_join_groups, can_read_all_group_messages, supports_inline_queries, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
    await cur.execute(
        query,
        (
            from_user.id,
            from_user.username,
            button_name,
            time,
            from_user.first_name,
            from_user.last_name,
            int(from_user.is_bot) if from_user.is_bot else None,
            from_user.language_code,
            int(from_user.is_premium) if from_user.is_premium else None,
            int(from_user.added_to_attachment_menu)
            if from_user.added_to_attachment_menu
            else None,
            int(from_user.can_join_groups) if from_user.can_join_groups else None,
            int(from_user.can_read_all_group_messages)
            if from_user.can_read_all_group_messages
            else None,
            int(from_user.supports_inline_queries)
            if from_user.supports_inline_queries
            else None,
            "True",
        ),
    )
    await bot.db_con.commit()


async def table_add_contact(data: tuple) -> None:
    cur = await bot.db_con.cursor()
    from_user, time, active_writer, txt = data
    query = """
                INSERT INTO 
                    contacts 
                    (user_id, username, first_name, last_name, 
                    time, question, text_message)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """
    await cur.execute(
        query,
        (
            from_user.id,
            from_user.username,
            from_user.first_name,
            from_user.last_name,
            time,
            active_writer,
            txt,
        ),
    )
    await bot.db_con.commit()
