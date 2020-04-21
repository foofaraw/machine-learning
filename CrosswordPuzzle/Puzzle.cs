﻿using System.Collections.Generic;

namespace CrosswordPuzzle
{
    public class Puzzle
    {
        public Puzzle(char[,] board, List<string> words)
        {
            this.board = board;
            this.words = words;
        }

        /// <summary>
        /// Read with grid[row, col]
        /// </summary>
        public char[,] board;
        public List<string> words;

        public bool IsSolved()
        {
            int rows = board.GetLength(0);
            int cols = board.GetLength(1);

            for (int i = 0; i < rows; i++)
                for (int j = 0; j < cols; j++)
                    if (board[i, j] == 0) return false;
            return true;
        }
    }
}