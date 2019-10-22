all:
	pyinstaller --onefile ./gomoku.py
	mv ./dist/gomoku ./brain-gomoku-ai.exe

clean:
	rm brain-gomoku-ai

fclean: clean

re: fclean all
