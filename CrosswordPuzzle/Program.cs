using System;
using System.IO;
using System.Collections.Generic;

namespace CrosswordPuzzle
{
    class Program
    {
        static void Main(string[] args)
        {
            var puzzle = CreatePuzzle(0);
            PrintBoard(puzzle.board);
        }

        static Puzzle CreatePuzzle(int n)
        {
            string[] rows = File.ReadAllLines($"Data/puzzle{n}");

            char[,] board = new char[rows.Length, rows[0].Length];
            for (int i = 0; i < rows.Length; i++)
                for (int j = 0; j < rows[i].Length; j++)
                {
                    if (rows[i][j] == '#')
                        board[i, j] = '#';
                }

            string[] words = File.ReadAllLines($"Data/words{n}");
            return new Puzzle(board, new HashSet<string>(words));
        }

        static void PrintBoard(char[,] board)
        {
            int rows = board.GetLength(0);
            int cols = board.GetLength(1);
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < cols; j++)
                {
                    Console.Write(board[i, j] == 0 ? "_ " : $"{board[i, j]} ");
                }
                Console.Write(Environment.NewLine);
            }
        }

        static bool Solve(Puzzle puzzle)
        {
            if (puzzle.words.Count == 0)
            {
                return puzzle.IsSolved();
            }
            

        }
    }
}
