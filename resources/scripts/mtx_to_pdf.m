
% Call the main function with the directory to search
directory = '/home/lukas/TNL/matrices/mtx-matrices-50piv_withResults_pivVec_v310523';
% Set the output directory for saving the figures
outputDirectory = '/home/lukas/School/CVUT/FJFI/masters_thesis/github/masters_thesis/images/ch03/input-matrices';

% Define the matrices to visualize
MATRICES = {"fp", "c-22"};

for i = 1 : length(MATRICES)
    processMTXFile(directory, MATRICES{i}, outputDirectory);
end

function processMTXFile(inputDir, targetBasename, outputDir)
    % Search the directory recursively for .mtx files
    filePattern = fullfile(inputDir, '**/*.mtx');
    files = dir(filePattern);

    n = numel(files);
    
    % Iterate over the found .mtx files
    for i = 1:n
        filePath = fullfile(files(i).folder, files(i).name);
        
        % Check if the basename matches the target
        [~, filename, ~] = fileparts(filePath);
        if strcmp(filename, targetBasename) % 1 == 1
            
            fprintf("[%d / %d] Reading matrix file: %s", i, n, filename)
            mtx = mread(filePath);

            res = 125;
            
            fprintf("\tGenerating the output figure...")
            [~, img, ~] = cspy(mtx, res);

            [m1, n1] = size (mtx) ;

            % Get the thumbnail of the matrix
            S = cs_thumb (mtx, res) ;
            [m, n] = size (S) ;

            % Draw the matrix
            image (img);
            axis equal ;
            axis ([-1 n+1 -1 m+1]) ;
            axis off
            
            % Draw a box around the whole matrix
            e = ceil (max (m1,n1) / max (m,n)) ;    % scale factor
            hold on
            drawbox (1,m1+1,1,n1+1,'k',1,e) ;
            hold off
            
            fprintf(" && Saving the output figure as a PDF file...")
            outputFilename = fullfile(outputDir, [filename, '.pdf']);
            exportgraphics(gcf, outputFilename);
            
            % Close the figure
            close(gcf);
            fprintf(" && Done.\n")
            
            % Exit the loop if the target file is found
            return;
        end
    end
    
    % If the loop completes without finding the target file
    disp(['Target file "', targetBasename, '.mtx" not found.']);
end

function drawbox (r1,r2,c1,c2,color,w,e)
    %DRAWBOX draw a box around a submatrix in the figure.
    %   Used by cspy, cs_dmspy, and ccspy.
    %   Example:
    %       drawbox (r1,r2,c1,c2,color,w,e)
    %   See also drawboxes, plot
    
    % CSparse, Copyright (c) 2006-2022, Timothy A. Davis. All Rights Reserved.
    % SPDX-License-Identifier: LGPL-2.1+
    
    if (r1 == r2 | c1 == c2)                                                    %#ok
        return
    end
    
    if (e == 1)
        r1 = r1 - .5 ;
        r2 = r2 - .5 ;
        c1 = c1 - .5 ;
        c2 = c2 - .5 ;
    else
        r1 = ceil (r1 / e) - .5 ;
        r2 = ceil ((r2 - 1) / e) + .5 ;
        c1 = ceil (c1 / e) - .5 ;
        c2 = ceil ((c2 - 1) / e) + .5 ;
    end
    
    if (c2 > c1 | r2 > r1)                                                      %#ok
        plot ([c1 c2 c2 c1 c1], [r1 r1 r2 r2 r1], color, 'LineWidth', w) ;
    end
end
