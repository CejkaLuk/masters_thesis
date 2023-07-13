
% Call the main function with the directory to search
directory = '/home/lukas/TNL/decomposition/src/Benchmarks/Decomposers/scripts/mtx-matrices-full';
% Set the output directory for saving the csv
outputFile = '../ch03/decomposition-benchmarks/matrices-info/50-pivoting-matrices-conditional-numbers.csv';

c_numbers = getCondNumbersOfMatricesInDir(directory);
saveCellArrayToCSV(c_numbers, outputFile);

function c_numbers = getCondNumbersOfMatricesInDir(inputDir)
    % Search the directory recursively for .mtx files
    filePattern = fullfile(inputDir, '**/*.mtx');
    files = dir(filePattern);

    n = numel(files);

    c_numbers = cell(n+1, 2);
    c_numbers(1, 1) = {'matrix-name'};
    c_numbers(1, 2) = {'rows'};
    c_numbers(1, 3) = {'condition-number'};

    % Iterate over the found .mtx files
    for i = 1:n
        % Save matrix name
        filePath = fullfile(files(i).folder, files(i).name);
        [~, filename, ~] = fileparts(filePath);
        c_numbers(i+1, 1) = {filename};
        
        fprintf("[%d / %d] Reading matrix file: %s", i, n, filename)
        % Read the mtx file
        mtx = mread(filePath);

        % Save matrix dimensions
        [rows, ~] = size(mtx);
        c_numbers(i+1, 2) = {rows};

        fprintf("\tComputing condition number...")
        % Save matrix condition number
        c_num = cond(full(mtx));
        c_numbers(i+1, 3) = {c_num};
        fprintf("\tDone.\n")
    end
end

function saveCellArrayToCSV(cellArray, filename)
    % Convert the cell array to a table
    dataTable = cell2table(cellArray);
    
    % Write the table to a CSV file
    writetable(dataTable, filename, 'Delimiter', ',');
end