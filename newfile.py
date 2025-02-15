#Dictionary Test

Words = {
 "algorithm" : "A set of well-defined instructions for solving a problem or accomplishing a task.",
 
"analog" : "A signal that varies continuously over time, like the voltage in a circuit.",
 
"bandwidth" : "The range of frequencies that a communication channel can carry.",
 
"binary": "A system of representing numbers using only two digits, 0 and 1.",
 
"bit" : "The smallest unit of data in a computer, representing a single binary digit (0 or 1).",
 
"boolean Algebra": "A system of logic used in computer science to represent truth values (true or false) and operations on them.",
 
"cache": "A temporary storage area used to speed up data access by storing frequently used data.",
 
"circuit" : "A closed loop of electrical components that allows current to flow.",
 
"compiler" : "A program that translates source code written in a high-level programming language into machine code that a computer can execute.",
 
"data Structure": "A way of organizing and storing data in a computer.",
 
"debugging" : "The process of finding and fixing errors in computer programs.",
 
"digital" : "A signal that is discrete, meaning it can only take on a finite number of values.",
 
"dynamic Programming" : "A technique for solving complex problems by breaking them down into smaller, overlapping subproblems.",
 
"electromagnetic Spectrum," : "The range of all possible frequencies of electromagnetic radiation.",

"entropy": "A measure of disorder or randomness in a system.",
 
"frequency" : "The number of cycles per second of a periodic signal.",
 
"hardware" : "The physical components of a computer system, such as the CPU, memory, and storage.",

"heuristics" : "Rule-of-thumb methods used to solve problems that may not always guarantee the optimal solution.",
 
"interrupt" : "A signal that temporarily stops the execution of a program to handle a specific event.",
 
"kernel" : "The core of an operating system that manages the computer's resources.",
 
"linear Algebra" : "A branch of mathematics that deals with vectors, matrices, and linear transformations.",
 
"logic Gate" : "An electronic circuit that performs a logical operation, such as AND, OR, or NOT.",
 
"machine Learning" : "A type of artificial intelligence that allows computers to learn from data without explicit programming.",
 
"microprocessor" : "The central processing unit (CPU) of a computer, responsible for executing instructions.",
 
"network" : "A group of interconnected devices that can communicate with each other.",
 
"operating System" : "A program that manages the computer's resources and provides a user interface.",
 
"protocol" : "A set of rules that govern communication between devices.",
 
"software" : "The programs and data that run on a computer.",
 
"system Architecture" : "The overall design and structure of a computer system or software.",
 
"transformer": "An electrical device that changes the voltage of an alternating current (AC) signal"

}

while True:
	user=input("Search: ").lower()
	print(user, "-", Words[user])
	print("\n")

#hehe