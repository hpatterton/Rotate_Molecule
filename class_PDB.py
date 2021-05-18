import numpy

class PDB:

    def __init__(self, path):
        self.file_contents = self.ReadFile(path)

    def ReadFile(self, path):
        file_contents = []
        f = open(path,'r')
        for line in f:
            file_contents.append(line.rstrip('\n'))
        return file_contents

    def GetCoordinates(self):
        xyz_coordinates=[]
        for item in self.file_contents:
            if(item[0:6] == 'HETATM'):
                xyz_coordinates.append([float(item[31:39].strip()), float(item[39:47].strip()), float(item[47:55].strip())])
        coordinates = numpy.array(xyz_coordinates)
        return coordinates

    def GetConnections(self):
        connection = []
        field_width = 5
        number_of_first_atom = self.GetNumberofFirstAtom()
        for item in self.file_contents:
            if (item[0:6] == 'CONECT'):
                start_of_field = 7
                temp_list = []
                entry = item[start_of_field:start_of_field+field_width].strip()
                while (entry != '') and (start_of_field + field_width <= 70):
                    temp_list.append(int(entry)-number_of_first_atom)
                    start_of_field = start_of_field + field_width
                    entry = item[start_of_field:start_of_field + field_width].strip()
                connection.append(temp_list)
        return connection

    def GetNumberofFirstAtom(self):
        number_of_first_atom = -1
        i = 0
        while (i < len(self.file_contents) and self.file_contents[i][0:6] != 'HETATM'):
            i += 1
        if i < len(self.file_contents):
            if (self.file_contents[i][7:12].strip() != ''):
                number_of_first_atom = int(self.file_contents[i][7:12].strip())
        return number_of_first_atom

    def CenterMolecule(self, coordinates):
        x = self.CenterCoordinates(coordinates[:,0])
        y = self.CenterCoordinates(coordinates[:,1])
        z = self.CenterCoordinates(coordinates[:,2])
        temp = []
        for i in range(len(x)):
            temp.append([x[i], y[i], z[i]])
        coordinates = numpy.array(temp)
        return coordinates

    def CenterCoordinates(self, coordinates):
        coordinates_min = min(coordinates)
        coordinates_max = max(coordinates)
        coordinates_range = coordinates_max - coordinates_min
        coordinates_offset = coordinates_max - coordinates_range / 2
        for i in range(len(coordinates)):
            coordinates[i] = coordinates[i] - coordinates_offset
        return coordinates




