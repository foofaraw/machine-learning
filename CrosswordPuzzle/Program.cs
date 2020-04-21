using System;
using System.IO;
using System.Linq;
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

        

        static Puzzle Solve(Puzzle puzzle)
        {
            if (puzzle.words.Count == 0)
            {
                if (puzzle.IsSolved())
                {
                    return puzzle;
                }
                else
                {
                    return null;
                }
            }

            foreach (string word in puzzle.words)
            {
                Puzzle solution = new Puzzle(
                    FillWordIntoBoard(puzzle.board, word),
                    puzzle.words.Where(w => w != word).ToList());

                Puzzle result = Solve(solution);
                if (result != null)
                    return result;
            }
            return null;
        }

        static char[,] FillWordIntoBoard(char[,] board, string word)
        {
            int rows = board.GetLength(0);
            int cols = board.GetLength(1);

            for (int i = 0; i < rows; i++)
            {
                char[] saveRow = GetRow(board, i);

                for (int n = 0; n < word.Length; n++)
                {
                    if (board[i, n] == 0)
                    {
                        var room = new ArraySegment<char>(saveRow, n, word.Length);
                        if (room.Any(i => i != 0))
                        {

                        }
                    }
                }
            }

            return board;
        }

        static char[] GetColumn(char[,] arr, int col) 
            => Enumerable.Range(0, arr.GetLength(0)).Select(x => arr[x, col]).ToArray();

        static char[] GetRow(char[,] arr, int row) 
            => Enumerable.Range(0, arr.GetLength(1)).Select(x => arr[row, x]).ToArray();

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
            return new Puzzle(board, new List<string>(words));
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
    }
}
